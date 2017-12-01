if count == 15:
    # print(">>", match.group(1), count)
    if "every day" in input_str:
        # since, current fix reminders are passed to temp register and then alarmed from tmp register
        if PARAM_REMIND[0][2] == PARAM_TMPREM[2]:
            PARAM_REMIND[0][1] += int(match.group(1))
        elif PARAM_REMIND[1][2] == PARAM_TMPREM[2]:
            PARAM_REMIND[1][1] += int(match.group(1))
        elif PARAM_REMIND[2][2] == PARAM_TMPREM[2]:
            PARAM_REMIND[2][1] += int(match.group(1))
    else:
        PARAM_TMPREM[1] += int(match.group(1))
        PARAM_TMPREM[3] = 1
if count == 16:
    # print(">>", match.group(1), count)
    if "every day" in input_str:
        # since, current fix reminders are passed to temp register and then alarmed from tmp register
        if PARAM_REMIND[0][2] == PARAM_TMPREM[2]:
            PARAM_REMIND[0][0] += int(match.group(1))
        elif PARAM_REMIND[1][2] == PARAM_TMPREM[2]:
            PARAM_REMIND[1][0] += int(match.group(1))
        elif PARAM_REMIND[2][2] == PARAM_TMPREM[2]:
            PARAM_REMIND[2][0] += int(match.group(1))
    else:
        PARAM_TMPREM[0] += int(match.group(1))
        PARAM_TMPREM[3] = 1
if count == 17:
    # print(">>", match.group(1), match.group(2), count)
    if "every day" in input_str:
        # since, current fix reminders are passed to temp register and then alarmed from tmp register
        if PARAM_REMIND[0][2] == match.group(1):
            PARAM_REMIND[0][1] += int(match.group(2))
        elif PARAM_REMIND[1][2] == match.group(1):
            PARAM_REMIND[1][1] += int(match.group(2))
        elif PARAM_REMIND[2][2] == match.group(1):
            PARAM_REMIND[2][1] += int(match.group(2))
    else:
        PARAM_TMPREM[1] += int(match.group(1))
        PARAM_TMPREM[3] = 1
if count == 18:
    # print(">>", match.group(1), match.group(2), count)
    if "every day" in input_str:
        # since, current fix reminders are passed to temp register and then alarmed from tmp register
        if PARAM_REMIND[0][2] == match.group(1):
            PARAM_REMIND[0][0] += int(match.group(2))
        elif PARAM_REMIND[1][2] == match.group(1):
            PARAM_REMIND[1][0] += int(match.group(2))
        elif PARAM_REMIND[2][2] == match.group(1):
            PARAM_REMIND[2][0] += int(match.group(2))
    else:
        PARAM_TMPREM[0] += int(match.group(1))
        PARAM_TMPREM[3] = 1
if count == 19:
    # print(">>", match.group(1), "|", match.group(2), "|", match.group(3), "|", count)
    if "every day" in input_str:
        # since, current fix reminders are passed to temp register and then alarmed from tmp register
        if PARAM_REMIND[0][2] == match.group(1):
            PARAM_REMIND[0][0] = int(match.group(2))
            PARAM_REMIND[0][1] = int(match.group(3))
        elif PARAM_REMIND[1][2] == match.group(1):
            PARAM_REMIND[1][0] = int(match.group(2))
            PARAM_REMIND[1][1] = int(match.group(3))
        elif PARAM_REMIND[1][2] == match.group(1):
            PARAM_REMIND[2][0] = int(match.group(2))
            PARAM_REMIND[2][1] = int(match.group(3))
    else:
        PARAM_TMPREM[0] = int(match.group(2))
        PARAM_TMPREM[1] = int(match.group(3))
        PARAM_TMPREM[2] = match.group(1)
        PARAM_TMPREM[3] = 1