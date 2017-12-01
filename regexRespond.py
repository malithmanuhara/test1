import random

from pronounObj import pronoun_obj
from functionalParam import pronouns
from chatOut import chat_out


# Respond to a chat input
def regex_respond(match, response):
    # pick a random response for the matched pattern
    random_resp = random.choice(response)
    # Replace wild cards with block of user input
    resp, obj_str = set_wildcard_strings(random_resp, match)
    # remove any unwanted strings from user input
    if resp[-2:] == '?.':
        resp = resp[:-2] + '.'
    chat_out(resp, 0)
    return obj_str


def set_wildcard_strings(random_resp, match):
    # find the position of the regex pattern
    pos = random_resp.find('%')
    # catch any object
    obj_str = "NULL"
    # check for multiple patterns
    while pos >= 0:
        num = int(random_resp[pos + 1:pos + 2])
        # create the response with substituted pronouns
        obj_str = match.group(num)
        print(obj_str)
        random_resp = random_resp[:pos] + substitute_pronouns(obj_str) + random_resp[pos + 2:]
        pos = random_resp.find('%')
        # Return the object by selecting the regex match with largest integer
    if obj_str is "NULL":
        obj_str = match.group(1)
    return random_resp, obj_str


# substituted pronouns of the user input string
def substitute_pronouns(input_str):
    substitute_str = pronoun_obj.sub(lambda mo: pronouns[mo.string[mo.start():mo.end()]], input_str.lower())
    return substitute_str
