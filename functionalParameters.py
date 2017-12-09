"""
    ############################################################
    Parameters required for stating functional behaviours
"""

"""
    ############################################################
    Random check for executing an extended chat with question or feedback
"""

RANDOM_CHECK = 9


"""
    ############################################################
    YES NO identifiers
"""


YES_TAG = ("yes", "sure", "ok", "okay")
NO_TAG = ("no", "nope", "dont", "do not")


"""
    ############################################################
    TAG Expander
"""


TAG_EXPANDER = {}
TAG_EXPANDER["FAV_BOOK"] = "favourite book"
TAG_EXPANDER["LRD_BOOK"] = "last read book"
TAG_EXPANDER["MRD_BOOK"] = "most read book"
TAG_EXPANDER["FAV_FOOD"] = "favourite food"
TAG_EXPANDER["MEA_FOOD"] = "most eat food"


"""
    ############################################################
    <TAG> Identification for feedback response generation
"""


TAG_DIC = {}

TAG_DIC["book_FAV_BOOK"] = "gamperaliya"
TAG_DIC["book_LRD_BOOK"] = "uganthaya"
TAG_DIC["book_MRD_BOOK"] = "viragaya"

TAG_DIC["novel_FAV_BOOK"] = "madoldoowa"
TAG_DIC["novel_LRD_BOOK"] = "oliver twist"
TAG_DIC["novel_MRD_BOOK"] = "harry potter"

TAG_DIC["short story_FAV_BOOK"] = "the red"
TAG_DIC["short story_LRD_BOOK"] = "the last one"
TAG_DIC["short story_MRD_BOOK"] = "geckos"

TAG_DIC["newspaper_FAV_BOOK"] = "sunday times"
TAG_DIC["newspaper_LRD_BOOK"] = "sunday observer"
TAG_DIC["newspaper_MRD_BOOK"] = "daily mirror"

TAG_DIC["magazine_FAV_BOOK"] = "iet"
TAG_DIC["magazine_LRD_BOOK"] = "airport review"
TAG_DIC["magazine_MRD_BOOK"] = "ieee"

TAG_DIC["food_FAV_FOOD"] = "bread"
TAG_DIC["food_MEA_FOOD"] = "cereals"

TAG_DIC["drink_FAV_FOOD"] = "tea"
TAG_DIC["drink_MEA_FOOD"] = "coffee"

TAG_DIC["sweet_FAV_FOOD"] = "chocolate"
TAG_DIC["sewwt_MEA_FOOD"] = "toffee"

TAG_DIC["candy_FAV_FOOD"] = "chocolate"
TAG_DIC["candy_MEA_FOOD"] = "toffee"

TAG_DIC["desert_FAV_FOOD"] = "cake"
TAG_DIC["desert_MEA_FOOD"] = "ice cream"

TAG_DIC["fruit_FAV_FOOD"] = "apple"
TAG_DIC["fruit_MEA_FOOD"] = "mango"

TAG_DIC["gamperaliya_AUT_BOOK"] = "martin wickramasinge"
TAG_DIC["gamperaliya_LAN_BOOK"] = "sinhala"
TAG_DIC["gamperaliya_TYP_BOOK"] = "novel"

TAG_DIC["oliver twist_AUT_BOOK"] = "charles dickens"
TAG_DIC["oliver twist_LAN_BOOK"] = "english"
TAG_DIC["oliver twist_TYP_BOOK"] = "novel"

TAG_DIC["apple_GOD_FOOD"] = "heart attack"
TAG_DIC["apple_BAD_FOOD"] = "skin decease"
TAG_DIC["apple_NUT_FOOD"] = "vitamin"

TAG_DIC["tea_GOD_FOOD"] = "coleserol"
TAG_DIC["tea_BAD_FOOD"] = "diaberes"
TAG_DIC["tea_NUT_FOOD"] = "minerals"

TAG_DIC["uganthaya_AUT_BOOK"] = "martin wickramasinge"
TAG_DIC["uganthaya_LAN_BOOK"] = "sinhala"
TAG_DIC["uganthaya_TYP_BOOK"] = "novel"


"""
    ############################################################
    Action dictionary
"""


ACTION_DIC = {}
ACTION_DIC[7] = "BRING"
ACTION_DIC[19] = "READ"
ACTION_DIC[23] = "REMIND1"
ACTION_DIC[24] = "REMIND2"
ACTION_DIC[25] = "REMIND3"
ACTION_DIC[26] = "REMIND4"



"""
    ############################################################
    Reminders
"""


REMIND_DIC = [[12, 40, "breakfast", 1], [18, 29, "lunch", 1], [20, 2, "dinner", 1], [8, 30, "morning medicine", 1], [13, 30, "after noon medicine", 1], [20, 30, "evening medicine", 1]]
