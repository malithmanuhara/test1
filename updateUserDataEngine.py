"""
    ############################################################
    Update user data
"""

from chatEngine import run_chat_engine
from generalFunctions import make_lower
from functionalParameters import TAG_EXPANDER
from functionalParameters import TAG_DIC
from generalFunctions import flash_string


def run_update_user_data_engine(chat_in, current_state_data):

    next_state_data = "null-action", "null-object", "null-tag", "null-tag-object"

    tag_string = current_state_data[1] + "_" + current_state_data[2]
    print("update - ", tag_string)
    TAG_DIC[tag_string] = chat_in
    flash_string("wow that is great to know your new " + str(TAG_EXPANDER[current_state_data[2]]))
    chat_in_phrase = str(make_lower(current_state_data[0])) + " " + str(current_state_data[1])
    chat_out, next_state_id, next_state_data = run_chat_engine(chat_in_phrase, next_state_data)
    return chat_out, next_state_id, next_state_data
