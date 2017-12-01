import datetime
import time
from objectParam import PARAM_REMIND
from objectParam import SALUTATION
from chatOut import chat_out
import functionalParam

PARAM_TMPREM = [7, 23, "temp_reminder", 0]


def remind_bot():

    #print("Time :", datetime.datetime.now())

    while 1:
        t_now = datetime.datetime.now()

        for i in PARAM_REMIND:
            if t_now.hour == i[0] and t_now.minute == i[1] and i[3] == 1:
                # current alarm is disabled for restricting one time occurrence
                i[3] = 0
                # Store the current reminder time in temporary location.
                # Fix reminders are passed to temp register and then alarmed from tmp register
                PARAM_TMPREM[0] = i[0]
                PARAM_TMPREM[1] = i[1]
                PARAM_TMPREM[2] = i[2]
                PARAM_TMPREM[3] = 1

                #print("reminder for ", i[2], " @ Hr ", i[0], " Mn ", i[1])
            elif t_now.hour == 0 and t_now.minute == 0:
                # enable all alarms at 12 midnight
                i[3] = 1

            # tmp register
            if t_now.hour == PARAM_TMPREM[0] and t_now.minute == PARAM_TMPREM[1] and PARAM_TMPREM[3] == 1:
                # current alarm is disabled for restricting one time occurrence
                PARAM_TMPREM[3] = 0
                # alarm
                chat_out(SALUTATION[0] + " it is time for your " + str(PARAM_TMPREM[2]), 1)
                functionalParam.REM_WAIT = "TRUE"

                time.sleep(20)

                if functionalParam.ACK_REM == "FALSE":
                    #print("rm >", functionalParam.REM_WAIT, " | ", functionalParam.ACK_REM)
                    functionalParam.REM_WAIT = "FALSE"
                    chat_out(SALUTATION[0] + " i will bring your " + str(PARAM_TMPREM[2]), 1)

    return


def acknowledge_reminder(count, obj_typ):
    if count == 1 and (obj_typ == "FOOD" or obj_typ == "MEDI") and functionalParam.REM_WAIT == "TRUE":
        functionalParam.ACK_REM = "TRUE"
        functionalParam.REM_WAIT = "FALSE"
        #print("ak > ", functionalParam.REM_WAIT, " | ", functionalParam.ACK_REM)
    return
