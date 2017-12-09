"""
    ############################################################
    Update Alarm
"""


import re
from unrecognizedChat import reply_unrecognized_chat
from functionalParameters import YES_TAG
from functionalParameters import REMIND_DIC


def run_update_alarm_engine(chat_in, current_state_data):

    next_state_data = "null-action", "null-object", "null-tag", "null-tag-object"
    yes_no_pattern = re.compile(r'(yes|sure|ok|okay|no|nope|dont|do not)( .*|)')
    match = yes_no_pattern.match(chat_in)

    alarm_tag = chat_in.split("_")
    if alarm_tag[0].strip() == "789alarm987":
        alarm_event = str(alarm_tag[1].strip())
        next_state_id = 4
        next_state_data = "null-action", alarm_event, "null-tag", "null-tag-object"
        chat_out = "it is time for your " + alarm_event
        print("ALARM ALARM ALARM")
        return chat_out, next_state_id, next_state_data
    elif match:
        print("conf rem update yes no match")
        if match.group(1) in YES_TAG:
            print("conf rem update yes")
            if current_state_data[1] == "null-object":
                print("conf rem update yes - 23 > count > 27")
                update_reminder_parameter(current_state_data[0], current_state_data[1], current_state_data[2])
                next_state_id = 0
                chat_out = "sure"
                return chat_out, next_state_id, current_state_data
            else:
                print("conf rem update yes - alarm direct update")
                update_reminder_parameter(current_state_data[0], current_state_data[1], current_state_data[2])
                next_state_id = 0
                chat_out = "sure"
                return chat_out, next_state_id, current_state_data

        else:
            print("conf rem update no")
            if current_state_data[1] == "null-object":
                print("conf rem update yes - 23 > count > 27")
                next_state_id = 0
                chat_out = "sure, no worries"
                return chat_out, next_state_id, current_state_data
            else:
                print("conf rem update yes - alarm direct update")
                next_state_id = 4
                chat_out = "sure, no worries"
                return chat_out, next_state_id, current_state_data
    else:
        next_state_id = 0
        chat_out = reply_unrecognized_chat()
        return chat_out, next_state_id, next_state_data


"""
    ############################################################
    Update Alarm Parameter
"""


def update_reminder_parameter(match, reminder_event, count):

    if reminder_event == "null-object":
        print("update request initiated from chat engine")
        for i in REMIND_DIC:
            if count == 23 or count == 25:
                if i[2] == str(match.group(1)) and str(match.group(3)) == "minutes":
                    print("match found 23 25 m")
                    i[1] += int(match.group(2))
                    i[3] = 1
                    print(REMIND_DIC)
                    return
                elif i[2] == str(match.group(1)) and str(match.group(3)) == "hours":
                    print("match found 23 25 h")
                    i[0] += int(match.group(2))
                    i[3] = 1
                    print(REMIND_DIC)
                    return
                else:
                    print("no match found 23 25")
            if count == 24 or count == 26:
                if i[2] == str(match.group(1)):
                    print("match found 24 26")
                    i[0] = int(match.group(2))
                    i[1] = int(match.group(3))
                    i[3] = 1
                    print(REMIND_DIC)
                    return
                else:
                    print("no match found 24 26")
            else:
                print("no match found")

    else:
        print("update request initiated from alarm")
        for i in REMIND_DIC:
            if i[2] == reminder_event and str(match.group(2)) == "minutes":
                print("match found")
                i[1] += int(match.group(1))
                i[3] = 1
                print(REMIND_DIC)
                return
            elif i[2] == reminder_event and str(match.group(2)) == "hours":
                print("match found")
                i[0] += int(match.group(1))
                i[3] = 1
                print(REMIND_DIC)
                return
            else:
                print("no match found")

    return
