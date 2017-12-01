import random
import fileinput
from chatOut import chat_out
from objectParam import PARAM_REMIND
from remindBot import PARAM_TMPREM
import functionalParam


# Respond to a chat input
def update_reminder(input_str, match, response, count):
    # pick a random response for the matched pattern
    random_resp = random.choice(response)
    update(input_str, match, count)
    functionalParam.ACK_REM = "TRUE"
    functionalParam.REM_WAIT = "FALSE"
    chat_out(random_resp, 0)
    return


def update(input_str, match, count):

    text_to_search1 = 'PARAM_REMIND = [[' + str(PARAM_REMIND[0][0]) + ', ' + str(PARAM_REMIND[0][1]) + ', "' + \
                       PARAM_REMIND[0][2] + '", ' + str(PARAM_REMIND[0][3]) + '], [' + str(PARAM_REMIND[1][0]) + ', ' + str(PARAM_REMIND[1][1]) + ', "' + \
                       PARAM_REMIND[1][2] + '", ' + str(PARAM_REMIND[1][3]) + '], [' + str(PARAM_REMIND[2][0]) + ', ' + \
                       str(PARAM_REMIND[2][1]) + ', "' + PARAM_REMIND[2][2] + '", ' + str(PARAM_REMIND[2][3]) + '], [' + \
                       str(PARAM_REMIND[3][0]) + ', ' + str(PARAM_REMIND[3][1]) + ', "' + PARAM_REMIND[3][2] + '", ' + \
                       str(PARAM_REMIND[3][3]) + '], [' + str(PARAM_REMIND[4][0]) + ', ' + str(PARAM_REMIND[4][1]) + ', "' + \
                       PARAM_REMIND[4][2] + '", ' + str(PARAM_REMIND[4][3]) + '], [' + str(PARAM_REMIND[5][0]) + ', ' + \
                       str(PARAM_REMIND[5][1]) + ', "' + PARAM_REMIND[5][2] + '", ' + str(PARAM_REMIND[5][3]) + ']]'

    # no need to file update the tmp register
    text_to_search2 = 'PARAM_TMPREM = [' + str(PARAM_TMPREM[0]) + ', ' + str(PARAM_TMPREM[1]) + ', "' + \
                     PARAM_TMPREM[2] + '", ' + str(PARAM_TMPREM[3]) + ']'

    #print(">>", text_to_search1, "\n")
    # no need to file update the tmp register
    #print(">>", text_to_search2, "\n")

    #################################
    if "every day" in input_str:
        if count == 15:
            if match.group(2) == "minutes":
                for i in range(0, 5):
                    if PARAM_REMIND[i][2] == PARAM_TMPREM[2]:
                        PARAM_REMIND[i][1] += int(match.group(1))
            elif match.group(2) == "hours":
                for i in range(0, 5):
                    if PARAM_REMIND[i][2] == PARAM_TMPREM[2]:
                        PARAM_REMIND[i][0] += int(match.group(1))
        elif count == 16 or count == 18:
            if match.group(3) == "minutes":
                for i in range(0, 5):
                    if PARAM_REMIND[i][2] == match.group(1):
                        PARAM_REMIND[i][1] += int(match.group(2))
            elif match.group(2) == "hours":
                for i in range(0, 5):
                    if PARAM_REMIND[i][2] == match.group(1):
                        PARAM_REMIND[i][0] += int(match.group(2))
        elif count == 17 or count == 19:
            for i in range(0, 5):
                if PARAM_REMIND[i][2] == match.group(1):
                    PARAM_REMIND[i][0] = int(match.group(2))
                    PARAM_REMIND[i][1] = int(match.group(3))
    else:
        if count == 15:
            if match.group(2) == "minutes":
                PARAM_TMPREM[1] += int(match.group(1))
                PARAM_TMPREM[3] = 1
            elif match.group(2) == "hours":
                PARAM_TMPREM[0] += int(match.group(1))
                PARAM_TMPREM[3] = 1
        if count == 16 or count == 18:
            if match.group(2) == "minutes":
                PARAM_TMPREM[2] = match.group(1)
                PARAM_TMPREM[1] += int(match.group(2))
                PARAM_TMPREM[3] = 1
            elif match.group(2) == "hours":
                PARAM_TMPREM[2] = match.group(1)
                PARAM_TMPREM[0] += int(match.group(2))
                PARAM_TMPREM[3] = 1
        elif count == 17 or count == 19:
            PARAM_TMPREM[0] = int(match.group(2))
            PARAM_TMPREM[1] = int(match.group(3))
            PARAM_TMPREM[2] = match.group(1)
            PARAM_TMPREM[3] = 1
    #################################

    text_to_replace1 = 'PARAM_REMIND = [[' + str(PARAM_REMIND[0][0]) + ', ' + str(PARAM_REMIND[0][1]) + ', "' + \
                     PARAM_REMIND[0][2] + '", ' + str(PARAM_REMIND[0][3]) + '], [' + str(PARAM_REMIND[1][0]) + ', ' + str(PARAM_REMIND[1][1]) + ', "' + \
                     PARAM_REMIND[1][2] + '", ' + str(PARAM_REMIND[1][3]) + '], [' + str(PARAM_REMIND[2][0]) + ', ' + \
                     str(PARAM_REMIND[2][1]) + ', "' + PARAM_REMIND[2][2] + '", ' + str(PARAM_REMIND[2][3]) + '], [' + \
                     str(PARAM_REMIND[3][0]) + ', ' + str(PARAM_REMIND[3][1]) + ', "' + PARAM_REMIND[3][2] + '", ' + \
                     str(PARAM_REMIND[3][3]) + '], [' + str(PARAM_REMIND[4][0]) + ', ' + str(PARAM_REMIND[4][1]) + ', "' + \
                     PARAM_REMIND[4][2] + '", ' + str(PARAM_REMIND[4][3]) + '], [' + str(PARAM_REMIND[5][0]) + ', ' + \
                     str(PARAM_REMIND[5][1]) + ', "' + PARAM_REMIND[5][2] + '", ' + str(PARAM_REMIND[5][3]) + ']]'
    text_to_replace2 = 'PARAM_TMPREM = [' + str(PARAM_TMPREM[0]) + ', ' + str(PARAM_TMPREM[1]) + ', "' + \
                     PARAM_TMPREM[2] + '", ' + str(PARAM_TMPREM[3]) + ']'

    #print(">>", text_to_replace1, "\n")
    #print(">>", text_to_replace2, "\n")

    update_file(text_to_search1, text_to_replace1)
    # no need to file update the tmp register
    #update_file(text_to_search2, text_to_replace2)

    return


def update_file(text_to_search, text_to_replace):

    # Update the files with new preference
    file_to_update = "objectParam.py"

    # Write to file
    with fileinput.FileInput(file_to_update, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(text_to_search, text_to_replace), end='')

    return
