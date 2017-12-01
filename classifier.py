import random
import re
import functionalParam
from regexRespond import regex_respond
from generalChat import general_chat
from keywordDetector import keyword_detector
from actionClassifier import action_classifier
from regexPairs import pairs
from actionController import action_controller
from updateReminder import update_reminder
from remindBot import acknowledge_reminder

# Classify the user input based on request chat/general chat


def classifier(input_str):
    # Variable to store the matched regex item
    count = 0

    # Create regex pairs object
    regex_pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]

    # check each pattern
    for (pattern, response) in regex_pairs:
        match = pattern.match(input_str)
        count += 1
        # if a matching pattern found
        if match:
            # The response is related to a reminder
            if 19 >= count >= 15:
                update_reminder(input_str, match, response, count)
                return
            # Generate a random number in between 0 to 9 and compare the value with CLASSIFIER_RAND_VAL
            elif random.randrange(0, 9) > functionalParam.CLASSIFIER_RAND_VAL:
                # Find a suitable respond for the matched regex
                obj_str = regex_respond(match, response)
                obj_str_2, obj_typ, obj_cat = keyword_detector(input_str)
                acknowledge_reminder(count, obj_typ)
                action_controller(count, obj_str)
                return

            else:
                # Find a known keyword for a long chat
                obj_str_1 = regex_respond(match, response)
                #obj_str_2,  = keyword_detector_classifier(input_str, count)
                obj_str_2, obj_typ, obj_cat = keyword_detector(input_str)
                acknowledge_reminder(count, obj_typ)
                action_classifier_str = str(count) + "_" + obj_typ + "_" + obj_cat + "_" + obj_str_2
                resp = action_classifier(action_classifier_str, obj_cat, count)
                if obj_cat == "TYP":
                    action_controller(count, obj_str_1)
                else:
                    action_controller(count, obj_str_2)
                return resp

    # if a matching pattern not found
    resp = general_chat(input_str)
    return resp
