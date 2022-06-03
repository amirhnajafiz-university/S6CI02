import simplejson
from fuzz.fuzz import EFS


def initialize():
    # create a EFS instance
    f = EFS()

    # TODO: create our parameters
    # -----

    # -----

    return f


def fuzzify(input):
    system = initialize()
    res = {}
    
    for x in input.keys():
        res[x] = system.Input(x, input.get(x))
    
    return res
