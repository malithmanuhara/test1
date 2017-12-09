"""
    ############################################################
    Functionality supporting the MainState
"""

import random
from functionalParameters import *
from generalFunctions import classifier
from generalFunctions import set_wildcard_strings
from generalFunctions import keyword_detector
from actionClassifier import action_classifier
from unrecognizedChat import reply_unrecognized_chat


"""
    ############################################################
    Chat Engine
"""


def run_chat_engine(chat_in, current_state_data):

    print("run_chat_engine", chat_in)

    next_state_data = "null-action", "null-object", "null-tag", "null-tag-object"

    match, response, count = classifier(chat_in)
    # No matching regular expression found for the chat input
    if match == "no-match-available" and response == "no-response-available":
        # Lookout for alarms
        alarm_tag = chat_in.split("_")
        if alarm_tag[0].strip() == "789alarm987":
            print("ALARM ALARM ALARM")
            alarm_event = str(alarm_tag[1].strip())
            next_state_id = 4
            next_state_data = "null-action", alarm_event, "null-tag", "null-tag-object"
            chat_out = "it is time for your " + alarm_event
            return chat_out, next_state_id, next_state_data
        else:
            print("unrecognized")
            next_state_id = 0
            chat_out = reply_unrecognized_chat()
            return chat_out, next_state_id, next_state_data
    else:
        if 22 < count < 27:
            print("reminder 22 < count < 27 - ", count)
            next_state_id = 5
            next_state_data = match, "null-object", count, "null-tag-object"
            selected_response = random.choice(response)
            chat_out = set_wildcard_strings(selected_response, match)
            return chat_out, next_state_id, next_state_data
        else:
            selected_response = random.choice(response)
            # Random check for initiating a extended chat
            # Do not initiate an extended chat
            if random.randrange(0, 9) > RANDOM_CHECK:
                chat_out = set_wildcard_strings(selected_response, match)
                next_state_id = 0
                return chat_out, next_state_id, next_state_data
            # Initiate an extended chat
            else:
                # Check if known keywords are found
                try:
                    keyword, keyword_type, keyword_category = keyword_detector(match.group(1))
                except IndexError:
                    keyword = "no-key-word-available"
                # No known key word found
                if keyword == "no-key-word-available":
                    chat_out = set_wildcard_strings(selected_response, match)
                    next_state_id = 0
                    return chat_out, next_state_id, next_state_data
                # Known key word found
                else:
                    action_classifier_phrase = ACTION_DIC[count] + "_" + keyword_type + "_" + keyword_category + "_" + keyword
                    # Classify and execute chat respond based on feedback or questing
                    chat_out, next_state_id, next_state_data = action_classifier(action_classifier_phrase)
                    return chat_out, next_state_id, next_state_data
