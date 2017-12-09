"""
    ############################################################
    Provide the response for the reply given for question asked by the
    robot.
    This function is executed in QuestionFeedbackState
"""

import re
import random
from functionalParameters import RANDOM_CHECK
from functionalParameters import TAG_EXPANDER
from chatEngine import run_chat_engine
from generalFunctions import keyword_detector
from generalFunctions import make_lower
from functionalParameters import YES_TAG
from functionalParameters import NO_TAG


def run_question_feedback_engine(chat_in, current_state_data):

    next_state_data = "null-action", "null-object", "null-tag", "null-tag-object"
    yes_no_pattern = re.compile(r'(yes|sure|ok|okay|no|nope|dont|do not|)( .*|)')
    match = yes_no_pattern.match(chat_in)

    if match:
        # Response is YES/NO only
        if match.group(2) == "":
            # Response is YES only
            if match.group(1) in YES_TAG:
                print("Response is YES only")
                if current_state_data[3] == "null-tag-object":
                    print("null-tag-object")
                    chat_in_phrase = str(make_lower(current_state_data[0])) + " " + str(current_state_data[1])
                    chat_out, next_state_id, next_state_data = run_chat_engine(chat_in_phrase, next_state_data)
                    return chat_out, next_state_id, next_state_data
                else:
                    print("valid tag object")
                    chat_in_phrase = str(make_lower(current_state_data[0])) + " " + str(current_state_data[3])
                    chat_out, next_state_id, next_state_data = run_chat_engine(chat_in_phrase, next_state_data)
                    return chat_out, next_state_id, next_state_data
            # Response is NO only
            elif match.group(1) in NO_TAG:
                print("Response is NO only")
                # Random check for updating user data or not
                # Update user data
                if random.randrange(0, 9) < RANDOM_CHECK and current_state_data[3] != "null-tag-object":
                    update_request = "is there a new " + str(TAG_EXPANDER[current_state_data[2]])
                    print("Update user data - ", update_request)
                    chat_out = update_request
                    next_state_id = 2
                    return chat_out, next_state_id, current_state_data
                # Not update user data
                else:
                    print("Not update user data")
                    chat_in_phrase = str(make_lower(current_state_data[0])) + " " + str(current_state_data[1])
                    chat_out, next_state_id, next_state_data = run_chat_engine(chat_in_phrase, next_state_data)
                    return chat_out, next_state_id, next_state_data
            else:
                return pattern_mismatched(chat_in, current_state_data)
        # Response is YES/NO ++++
        else:
            # Response is YES ++++
            if match.group(1) in YES_TAG:
                print("Response is YES ++++")
                chat_out, next_state_id, next_state_data = run_chat_engine(match.group(2).strip(), next_state_data)
                return chat_out, next_state_id, next_state_data
            # Response is NO ++++
            elif match.group(1) in NO_TAG:
                print("Response is NO ++++")
                chat_out, next_state_id, next_state_data = run_chat_engine(match.group(2).strip(), next_state_data)
                return chat_out, next_state_id, next_state_data
            else:
                return pattern_mismatched(chat_in, current_state_data)
    else:
        print("No match found")
        return pattern_mismatched(chat_in, current_state_data)

"""
    ############################################################
    If pattern mismatched
"""


def pattern_mismatched(chat_in, current_state_data):

    next_state_data = "null-action", "null-object", "null-tag"

    if keyword_detector(chat_in):
        # Create response tag
        print("keyword detected for mismatch")
        chat_in_phrase = str(make_lower(current_state_data[0])) + " " + str(chat_in)
        chat_out, next_state_id, next_state_data = run_chat_engine(chat_in_phrase, next_state_data)
        return chat_out, next_state_id, next_state_data
    else:
        print("no keyword detected for mismatch")
        chat_out, next_state_id, next_state_data = run_chat_engine(chat_in, next_state_data)
        return chat_out, next_state_id, next_state_data
