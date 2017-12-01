import random
import objectParam


# Respond to a chat input
def feedback_tag_expander(match, response):
    # pick a random response for the matched pattern
    random_resp = random.choice(response)
    # Replace wild cards with block of user input
    wildcard_object, wildcard_resp = set_wildcard_strings(random_resp, match)
    resp = set_tags(wildcard_resp, wildcard_object)
    # remove any unwanted strings from user input
    if resp[-2:] == '?.':
        resp = resp[:-2] + '.'
    return resp


def set_tags(wildcard_resp, wildcard_object):
    # find the position of the tag
    pos = wildcard_resp.find('<')
    # check for multiple tags
    while pos >= 0:
        # select the tag without <>
        tag = wildcard_resp[pos + 1:pos + 9]
        # create the response with substituted tags
        wildcard_resp = wildcard_resp[:pos] + substitute_tags(tag, wildcard_object) + wildcard_resp[pos + 10:]
        pos = wildcard_resp.find('<')
    return wildcard_resp


def substitute_tags(tag, wildcard_object):
    tag_string = wildcard_object + "_" + tag
    return objectParam.PARAM_DIC[tag_string]


def set_wildcard_strings(random_resp, match):
    # find the position of the regex pattern
    pos = random_resp.find('%')
    wildcard_object = "NULL"
    if pos >= 0:
        num = int(random_resp[pos + 1:pos + 2])
        # create the response with substituted wild card
        wildcard_object = match.group(num)
        random_resp = random_resp[:pos] + wildcard_object + random_resp[pos + 2:]
    return wildcard_object, random_resp

