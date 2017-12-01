#import nltk
import keywords
#from nltk import word_tokenize

# Filter the answer and check for yes/no reply


def answer_filter(input_str):
    # Tokenize
    #tokens = word_tokenize(input_str)
    # Create nltk sentence
    #sentence = nltk.Text(tokens)

    sentence = input_str.split(" ")

    for word in sentence:
        if word in keywords.YES_TAG:
            return "YES", input_str[4:]
        elif word in keywords.NO_TAG:
            return "NO", input_str[3:]

    return "NULL", input_str
