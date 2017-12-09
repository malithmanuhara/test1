"""
    ############################################################
    Alarm
"""


import re
from chatEngine import run_chat_engine
from generalFunctions import classifier


def run_alarm_engine(chat_in, current_state_data):

    next_state_data = "null-action", "null-object", "null-tag", "null-tag-object"
    update_alarm_pattern = re.compile(r'(?:can you |could you |)(?:please |)remind (?:me |)(?:in |by |)([0-9]{1,2}) (minutes|hours)(?: later|)(?: every day|)(?: please|)')
    # Alarm update is requested

    update_alarm_pattern_match = update_alarm_pattern.match(chat_in)

    alarm_tag = chat_in.split("_")
    if alarm_tag[0].strip() == "789alarm987":
        alarm_event = str(alarm_tag[1].strip())
        next_state_id = 4
        next_state_data = "null-action", alarm_event, "null-tag", "null-tag-object"
        chat_out = "it is time for your " + alarm_event
        print("ALARM ALARM ALARM")
        return chat_out, next_state_id, next_state_data
    elif update_alarm_pattern_match:
        # Alarm acknowledged
        print("update reminder direct")
        next_state_id = 5
        next_state_data = update_alarm_pattern_match, str(current_state_data[1]), "null-tag", "null-tag-object"
        chat_out = "are you sure you want to chang " + str(current_state_data[1]) + " time"
        print("are you sure you want to change " + str(current_state_data[1]) + " time")
        return chat_out, next_state_id, next_state_data
    else:
        match, response, count = classifier(chat_in)

        if match == "no-match-available" and response == "no-response-available":
            # force acknowledge
            next_state_id = 0
            chat_out = "you must take your " + str(current_state_data[1]) + " on time"
            print("you must take your " + str(current_state_data[1]) + " on time")
            return chat_out, next_state_id, next_state_data
        else:
            if count == 7:
                # Alarm acknowledged
                print("bring me some food")
                chat_out, next_state_id, next_state_data = run_chat_engine(chat_in, next_state_data)
                return chat_out, next_state_id, next_state_data
            elif 22 < count < 27:
                # Alarm acknowledged
                # next_state_id = 5
                # next_state_data = "null-action", str(current_state_data[1]), "null-tag", "null-tag-object"
                # chat_out = "are you sure you want to update " + str(current_state_data[1]) + " alarm time"
                # print("are you sure you want to update " + str(current_state_data[1]) + " alarm time")
                # return chat_out, next_state_id, next_state_data
                print("update reminder 22 < count < 27")
                chat_out, next_state_id, next_state_data = run_chat_engine(chat_in, next_state_data)
                return chat_out, next_state_id, next_state_data
            else:
                # force acknowledge
                next_state_id = 0
                chat_out = "you must take your " + str(current_state_data[1]) + " on time"
                print("you must take your " + str(current_state_data[1]) + " on time")
                return chat_out, next_state_id, next_state_data








