import re

from functionalParam import pronouns

# Sort and create pronoun object
def compile_pronoun(lst):
    sorted_pronoun = sorted(lst.keys(), key=len, reverse=True)
    return re.compile(r"\b({0})\b".format("|".join(map(re.escape, sorted_pronoun))), re.IGNORECASE)

# Create pronoun object
pronoun_obj = compile_pronoun(pronouns)