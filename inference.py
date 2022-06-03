import simplejson
from parser import getRules

"""
Begin method will get our inputs and will
return answers.
"""
def begin(inputs):
    # getting the rules
    rules = getRules()
    print(simplejson.dumps(rules, sort_keys=True, indent=4, use_decimal=True))
