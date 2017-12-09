"""
    ############################################################
    Classify the next action based on input type; next action requires a clarification
    or providing a feedback
"""

import re
import random
from regexPairs import feedback_regex_pairs
from regexPairs import question_regex_pairs
from functionalParameters import TAG_DIC

# Create regex keyword pairs object
feedback_regex_pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in feedback_regex_pairs]
question_regex_pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in question_regex_pairs]

"""
    ############################################################
    Classify based on keyword type
"""


def action_classifier(action_classifier_phrase):

    action, keyword_type, keyword_category, keyword = action_classifier_phrase.split("_")

    if keyword_category == "ITM":
        chat_out, next_state_id, next_state_data = generate_respond_feedback(action_classifier_phrase)

    elif keyword_category == "TYP":
        chat_out, next_state_id, next_state_data = generate_question_feedback(action_classifier_phrase)

    return chat_out, next_state_id, next_state_data


"""
    ############################################################
    Generate a feedback response for the chat input
"""


def generate_respond_feedback(action_classifier_phrase):

    # check matching feedback response pattern
    for (pattern, response) in feedback_regex_pairs:
        match = pattern.match(action_classifier_phrase)

        if match:
            selected_response = random.choice(response)
            chat_out, tag, tag_object = expand_tags(selected_response, match)
            print(chat_out)
            next_state_id = 0
            next_state_data = "null-action", "null-object", "null-tag"
            return chat_out, next_state_id, next_state_data

    # If no matching feedback response pattern found
    next_state_id = 0
    next_state_data = "null-action", "null-object", "null-tag", "null-tag-object"
    return "feedback response - " + str(action_classifier_phrase), next_state_id, next_state_data


"""
    ############################################################
    Generate a question response for the chat input
"""


def generate_question_feedback(action_classifier_phrase):
    # check matching feedback response pattern
    for (pattern, response) in question_regex_pairs:
        match = pattern.match(action_classifier_phrase)

        if match:
            selected_response = random.choice(response)
            chat_out, tag, tag_object = expand_tags(selected_response, match)
            # action_classifier_phrase =
            # ACTION_DIC[count] + "_" + keyword_type + "_" + keyword_category + "_" + keyword
            split_action_classifier_phrase = action_classifier_phrase.split("_")
            next_state_id = 1
            next_state_data = split_action_classifier_phrase[0], split_action_classifier_phrase[3], tag, tag_object
            return chat_out, next_state_id, next_state_data

    # If no matching question response pattern found
    next_state_id = 1
    next_state_data = "null-action", "null-object", "null-tag", "null-tag-object"
    return "feedback response - " + str(action_classifier_phrase), next_state_id, next_state_data


"""
    ############################################################
    Condition the matched action_classifier_phrase
"""


def expand_tags(response, match):
    # Replace wild cards with block of user input
    wildcard_response, wildcard_object = set_wildcard_strings(response, match)
    if wildcard_object == "no-wildcard_strings-available":
        return response, "null-tag", "null-tag-object"
    else:
        tagged_response, tag, tag_object = set_tags(wildcard_response, wildcard_object)
        return tagged_response, tag, tag_object


"""
    ############################################################
    find and replace feedback <> tags
"""


def set_tags(wildcard_resp, wildcard_object):
    # find the position of the tag
    pos = wildcard_resp.find('<')
    # check for multiple tags
    tag = "null-tag"
    tag_object = "null-tag-object"
    while pos >= 0:
        # select the tag without <>
        tag = wildcard_resp[pos + 1:pos + 9]
        # create the response with substituted tags
        tag_object = substitute_tags(tag, wildcard_object)
        wildcard_resp = wildcard_resp[:pos] + tag_object + wildcard_resp[pos + 10:]
        pos = wildcard_resp.find('<')
    return wildcard_resp, tag, tag_object

"""
    ############################################################
    Replace <> tags with suitable content available
"""


def substitute_tags(tag, wildcard_object):
    tag_string = wildcard_object + "_" + tag
    return TAG_DIC[tag_string]


"""
    ############################################################
    Condition regular expression respond
        Replace wild cards with block of user input
"""


def set_wildcard_strings(response, match):
    # find the position of the first regex replacement pattern
    pos = response.find('%')
    # check for multiple patterns
    if pos >= 0:
        # convert position of first regex replacement pattern to numerical value
        num = int(response[pos + 1:pos + 2])
        # find the substitution from the match and store
        regex_obj_str = match.group(num)
        response = response[:pos] + regex_obj_str + response[pos + 2:]
        return response, regex_obj_str
    else:
        return response, "no-wildcard_strings-available"
