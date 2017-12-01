import objectParam
import fileinput
from chatOut import chat_out
from chatIn import chat_in
from answerFilter import answer_filter
from functionalParam import ACTION_DIC

def update_db(wildcard_object, tag, tag_object, action_num):
    # Check if the user has actually changed his/her preference
    chat_out("Is there a new " + objectParam.PARAM_LST[tag], 0)
    resp = chat_in()
    yn_answer, filtered_resp = answer_filter(resp)
    #print(">>", yn_answer)

    # If the answer is NO; ie : User has not changed the preference
    if yn_answer is "NO":
        # Move back to general chat continuation
        chat_out("that is fine", 0)
        #print("NO UPDATE")
        return 0

    # If the answer is YES; ie : User has changed the preference
    elif yn_answer is "YES":

        # Check for the new preference
        chat_out("What is your new " + objectParam.PARAM_LST[tag], 0)
        new_value = chat_in()

        # Update the files with new preference
        file_to_update = "objectParam.py"
        text_to_search = 'PARAM_DIC["' + str(tag) + '"] = "' + objectParam.PARAM_DIC[tag] + '"'
        text_to_replace = 'PARAM_DIC["' + str(tag) + '"] = "' + new_value + '"'

        #print("file_to_search : ", file_to_update)
        #print("text_to_search : ", text_to_search)
        #print("text_to_replace : ", text_to_replace)

        objectParam.PARAM_DIC[tag] = new_value
        #print(objectParam.PARAM_LST[tag], " : ", objectParam.PARAM_DIC[tag])

        # Write to file
        with fileinput.FileInput(file_to_update, inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace(text_to_search, text_to_replace), end='')

        chat_out("i will " + ACTION_DIC[action_num] + " your new " + objectParam.PARAM_LST[tag] + " " + new_value)
        return new_value

    # If the user answer is too complicated or unable to understand; Only YN answers
    else:
        chat_out("pardon me", 0)
        return 0

