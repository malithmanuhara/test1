from respondGeneratorKeywordFeedback import respond_generator_keyword_feedback
from respondGeneratorKeywordQuestion import respond_generator_keyword_question


def action_classifier(action_classifier_str, obj_cat, count):
    if obj_cat == "ITM":
        resp = respond_generator_keyword_feedback(action_classifier_str)

    elif obj_cat == "TYP":
        respond_generator_keyword_question(action_classifier_str, count)

    return resp
