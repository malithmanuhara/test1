"""
    ############################################################
    Common functions required by other modules
"""

import re
from flask import flash
from regexPairs import regex_pairs
from regexPairs import keyword_regex_pairs

regex_pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in regex_pairs]
keyword_regex_pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in keyword_regex_pairs]


"""
    ############################################################
    Flask flash
"""


def flash_string(string, msg_type):
    flash(string, msg_type)


"""
    ############################################################
    Classify chat input
"""


def classifier(chat_in):
    count = 0
    for (pattern, response) in regex_pairs:
        match = pattern.match(chat_in)
        count += 1
        if match:
            return match, response, count

    return "no-match-available", "no-response-available", "no-count-available"


"""
    ############################################################
    Detect key words
"""


def keyword_detector(match_group_1):
    for (pattern, response) in keyword_regex_pairs:
        match = pattern.match(match_group_1)
        if match:
            # Assign the only response as keyword_type_category
            keyword_type_category = response
            keyword_type, keyword_category = keyword_type_category.split("_")
            return match.group(1), keyword_type, keyword_category
    return "no-key-word-available", "NULL", "NULL"


"""
    ############################################################
    Condition regular expression respond
        Replace wild cards with block of user input
"""


def set_wildcard_strings(response, match):
    # find the position of the first regex replacement pattern
    pos = response.find('%')
    # check for multiple patterns
    while pos >= 0:
        # convert position of first regex replacement pattern to numerical value
        num = int(response[pos + 1:pos + 2])
        # find the substitution from the match and store
        regex_obj_str = match.group(num)
        response = response[:pos] + regex_obj_str + response[pos + 2:]
        # find the position of the next regex replacement pattern
        pos = response.find('%')
    return response


"""
    ############################################################
    Convert chat input to lower case
"""


def make_lower(chat_in):
    chat_in_lower = chat_in.lower()
    return chat_in_lower


"""
    ############################################################
    Tokenize chat input
"""


def tokenize(chat_in):
    chat_in_tokenize = chat_in.split(" ")
    return chat_in_tokenize
