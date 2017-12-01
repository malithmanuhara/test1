import re
import keywords
import random
from regexPairsKeywordsQuestion import question_keyword_pairs
from questionTagExpander import question_tag_expander
from answerFilter import answer_filter
from functionalParam import UPDATEDB_RAND_VAL
from functionalParam import ACTION_DIC
from functionalParam import NULL_REPLY
from chatIn import chat_in
from chatOut import chat_out
from updateDB import update_db

# Respond to a chat input based on keywords by a feedback statement


def respond_generator_keyword_question(input_str, action_num):
    from classifier import classifier

    # Create regex keyword pairs object
    regex_pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in question_keyword_pairs]

    obj_str = "NULL"

    # check each pattern
    for (pattern, response) in regex_pairs:
        # print("input str - ", input_str)
        match = pattern.match(input_str)

        if match:
            # ask  a question for clarifications
            wildcard_object, tag, tag_object = question_tag_expander(match, response)

            resp = chat_in()
            yn_resp, filtered_resp = answer_filter(resp)
            # if a long answer is provided ex : yes bring me xxx
            if filtered_resp is not "":
                # Agreed for the robot suggestion
                if yn_resp is "YES":
                    classifier(filtered_resp)
                    return obj_str
                # New request not agreeing to robot suggestion
                elif yn_resp is "NO":
                    # Update the object parameters, user now has a different view
                    classifier(filtered_resp)
                    return obj_str
                # Direct new request
                else:
                    # check if the answer matches with available book/food item
                    if (resp in keywords.BOOK_ITM) or (resp in keywords.FOOD_ITM):
                        default_resp = (ACTION_DIC[action_num] + " " + resp)
                        classifier(default_resp)
                        obj_str = tag_object
                        return obj_str
                    # If not
                    else:
                        classifier(resp)
                        return obj_str
            else:
                # YES/NO answer
                if yn_resp is "YES":
                    if tag_object is "NULL":
                        chat_out(NULL_REPLY, 0)
                        respond_generator_keyword_question(input_str, action_num)
                        return obj_str
                    else:
                        default_resp = (ACTION_DIC[action_num] + " " + tag_object)
                        classifier(default_resp)
                        obj_str = tag_object
                        return obj_str
                # YES/NO answer
                elif yn_resp is "NO":
                    if tag_object is "NULL":
                        chat_out(NULL_REPLY, 0)
                        respond_generator_keyword_question(input_str, action_num)
                        return obj_str
                    else:
                        if random.randrange(0, 9) > UPDATEDB_RAND_VAL:
                            new_value = update_db(wildcard_object, tag, tag_object, action_num)
                            if new_value != 0:
                                return new_value
                            else:
                                respond_generator_keyword_question(input_str, action_num)
                                return obj_str
                        else:
                            respond_generator_keyword_question(input_str, action_num)
                            return obj_str
                # different answer
                else:
                    classifier(filtered_resp)
                    return obj_str
    return obj_str
