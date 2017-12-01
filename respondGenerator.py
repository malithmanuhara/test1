from nltk import word_tokenize
import nltk
import random

from classifier import classifier
import greetings


# Respond to a chat input
# Greetings and regular expressions based

def respond_generator(raw):
    # Convert to lowercase letters
    input_str = raw.lower()
    # Tokenize
    tokens = word_tokenize(input_str)
    # Create nltk sentence
    sentence = nltk.Text(tokens)

    for word in sentence:
        if word in greetings.GREETING_KEYWORDS_I:
            resp = random.choice(greetings.GREETING_RESPONSES_I)
            return resp
        elif word in greetings.GREETING_KEYWORDS_III:
            resp = random.choice(greetings.GREETING_KEYWORDS_III + greetings.GREETING_KEYWORDS_VI)
            return resp
    else:
        for word2 in greetings.GREETING_KEYWORDS_II:
            if input_str.find(word2) >= 0:
                resp = input_str + " to you sir"
                return resp
        else:
            for word3 in greetings.GREETING_KEYWORDS_VI:
                if input_str.find(word3) >= 0:
                    resp = random.choice(greetings.GREETING_KEYWORDS_III + greetings.GREETING_KEYWORDS_VI)
                    return resp
            else:

                resp = classifier(input_str)
                return resp
