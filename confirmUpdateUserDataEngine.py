"""
    ############################################################
    Confirm Update user data
"""

import re
from functionalParameters import YES_TAG
from functionalParameters import NO_TAG
from functionalParameters import TAG_EXPANDER
from chatEngine import run_chat_engine
from generalFunctions import make_lower
from generalFunctions import flash_string



def run_confirm_update_user_data_engine(chat_in, current_state_data):

    next_state_data = "null-action", "null-object", "null-tag", "null-tag-object"
    yes_no_pattern = re.compile(r'(yes|sure|ok|okay|no|nope|dont|do not|)( .*|)')
    match = yes_no_pattern.match(chat_in)

    alarm_tag = chat_in.split("_")
    if alarm_tag[0].strip() == "789alarm987":
        alarm_event = str(alarm_tag[1].strip())
        next_state_id = 4
        next_state_data = "null-action", alarm_event, "null-tag", "null-tag-object"
        chat_out = "it is time for your " + alarm_event
        print("ALARM ALARM ALARM")
        return chat_out, next_state_id, next_state_data
    else:
        if match:
            if match.group(1) in YES_TAG:
                print("conf update yes")
                chat_out = "What is the new " + str(TAG_EXPANDER[current_state_data[2]])
                next_state_id = 3
                return chat_out, next_state_id, current_state_data
            elif match.group(1) in NO_TAG:
                print("conf update no")
                flash_string("ok that is fine")
                chat_in_phrase = str(make_lower(current_state_data[0])) + " " + str(current_state_data[1])
                chat_out, next_state_id, next_state_data = run_chat_engine(chat_in_phrase, next_state_data)
                return chat_out, next_state_id, next_state_data
            else:
                print("conf update else, cant find any yes no input")
                chat_out, next_state_id, next_state_data = run_chat_engine(chat_in, next_state_data)
                return chat_out, next_state_id, next_state_data
        else:
            print("conf update else")
            chat_out, next_state_id, next_state_data = run_chat_engine(chat_in, next_state_data)
            return chat_out, next_state_id, next_state_data
