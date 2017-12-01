import re
from regexPairsKeywordsFeedback import feedback_keyword_pairs
from feedbackTagExpander import feedback_tag_expander

# Respond to a chat input based on keywords by a feedback statement


def respond_generator_keyword_feedback(input_str):

    # Create regex keyword pairs object
    regex_pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in feedback_keyword_pairs]

    # check each pattern
    for (pattern, response) in regex_pairs:
        match = pattern.match(input_str)

        if match:
            resp = feedback_tag_expander(match, response)
            return resp
    return "NO_MATCH_FOUND"

