import nltk
import keywords
from nltk import word_tokenize


def keyword_detector(input_str):

    # Tokenize
    tokens = word_tokenize(input_str)
    # Create nltk sentence
    sentence = nltk.Text(tokens)

    for obj_str in sentence:
        if obj_str in keywords.BOOK_ITM:
            return obj_str, "BOOK", "ITM"

        elif obj_str in keywords.BOOK_TYP:
            return obj_str, "BOOK", "TYP"

        elif obj_str in keywords.FOOD_ITM:
            return obj_str, "FOOD", "ITM"

        elif obj_str in keywords.FOOD_TYP:
            return obj_str, "FOOD", "TYP"

        elif obj_str in keywords.MEDI_ITM:
            return obj_str, "MEDI", "ITM"

        elif obj_str in keywords.MEDI_TYP:
            return obj_str, "MEDI", "TYP"

    return obj_str, "NULL", "NULL"
