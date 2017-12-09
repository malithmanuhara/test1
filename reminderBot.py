"""
    ############################################################
    Handles all the reminders
"""

import datetime
from functionalParameters import REMIND_DIC


def reminder_bot():

    TEMP_REMIND_DIC = [12, 12, "temp_reminder", 0]

    t_now = datetime.datetime.now()

    for i in REMIND_DIC:

        if t_now.hour == i[0] and t_now.minute == i[1] and i[3] == 1:
            # current alarm is disabled for restricting one time occurrence
            i[3] = 0
            # Store the current reminder time in temporary location.
            # Fix reminders are passed to temp register and then alarmed from tmp register
            TEMP_REMIND_DIC[0] = i[0]
            TEMP_REMIND_DIC[1] = i[1]
            TEMP_REMIND_DIC[2] = i[2]
            TEMP_REMIND_DIC[3] = 1

            print("reminder for ", i[2], " @ Hr ", i[0], " Mn ", i[1])

        elif t_now.hour == 0 and t_now.minute == 0:
            # enable all alarms at 12 midnight
            i[3] = 1

        # tmp register
        if t_now.hour == TEMP_REMIND_DIC[0] and t_now.minute == TEMP_REMIND_DIC[1] and TEMP_REMIND_DIC[3] == 1:
            # current alarm is disabled for restricting one time occurrence
            TEMP_REMIND_DIC[3] = 0
            # alarm
            alarm_string = "it is time for your " + str(TEMP_REMIND_DIC[2])
            print(alarm_string)

            return alarm_string

    return "no-alarm"
