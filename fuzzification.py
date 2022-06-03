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
    for x in input.keys():
        print(x, input.get(x))
        print(system.Input(x, input.get(x)))
