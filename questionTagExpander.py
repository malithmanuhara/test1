import random
import objectParam
from chatOut import chat_out


# Respond to a chat input
def question_tag_expander(match, response):
    # pick a random response for the matched pattern
    random_resp = random.choice(response)
    # Replace wild cards with block of user input
    wildcard_object, wildcard_resp = set_wildcard_strings(random_resp, match)
    tag, tag_object, resp = set_tags(wildcard_resp)
    # remove any unwanted strings from user input
    if resp[-2:] == '?.':
        resp = resp[:-2] + '.'
    # print("resp - ", resp, " - ", random_resp)
    chat_out(resp, 0)
    return wildcard_object, tag, tag_object


def set_tags(wildcard_resp):
    # find the position of the tag
    pos = wildcard_resp.find('<')
    tag_object = "NULL"
    if pos >= 0:
        # select the tag without <>
        tag = wildcard_resp[pos + 1:pos + 9]
        # create the response with substituted tags
        tag_object = substitute_tags(tag)
        wildcard_resp_new = wildcard_resp[:pos] + tag_object + wildcard_resp[pos + 10:]
        return tag, tag_object, wildcard_resp_new
    return "NULL", tag_object, wildcard_resp


def substitute_tags(tag):
    return objectParam.PARAM_DIC[tag]


def set_wildcard_strings(random_resp, match):
    # find the position of the regex pattern
    pos = random_resp.find('%')
    if pos >= 0:
        num = int(random_resp[pos + 1:pos + 2])
        # create the response with substituted wild card
        wildcard_object = match.group(num)
        random_resp = random_resp[:pos] + wildcard_object + random_resp[pos + 2:]
        return wildcard_object, random_resp
    return "NULL", random_resp

