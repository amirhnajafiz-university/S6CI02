from parameter.parameter import Parameter
from scipy import ndimage
import numpy as np
from decimal import Decimal


# scales
SCALE = 1000
# limits
LIMIT_Y = 0.1
LIMIT_X = 4

"""
this method will defuzzify our output.
"""
def defuzzify(input):
    # our output parameter
    output = Parameter()
    output.NewSession('healthy').Range([0.25, 1, 0.25]).LeftValue(1)
    output.NewSession('sick_1').Range([0, 2, 1])
    output.NewSession('sick_2').Range([1, 3, 2])
    output.NewSession('sick_3').Range([2, 4, 3])
    output.NewSession('sick_4').Range([3, 4, 4]).RightValue(1)

    # getting our center of mass
    y, x = calculate(create_ground(input, output))

    # translate
    x = round(Decimal(x / SCALE), 5) # revert the scaling
    res = ' & '.join(translate(x))

    return f'{res} : {x}'


"""
this method translates the output number to a set name.
"""
def translate(value):
    temp = []

    if value < 1.78:
        temp.append("Healthy")
    if value > 1 and value < 2.51:
        temp.append("Sick (s1)")
    if value > 1.78 and value < 3.25:
        temp.append("Sick (s2)")
    if value > 1.5 and value < 4.5:
        temp.append("Sick (s3)")
    if value > 3.25:
        temp.append("Sick (s4)")
    
    return temp


"""
this method will create our ground for us.
"""
def create_ground(values, p):
    # first we scale our ground
    scaled_x = int(LIMIT_X * SCALE)
    scaled_y = int(LIMIT_Y * SCALE)

    # create a empty ground
    ground = np.zeros((scaled_y, scaled_x))

    # loop into our values
    for key in values.keys():
        # first we get the session
        v = values.get(key)
        for y in range(scaled_y):  # loop in y
            y_prime = float(y / SCALE)
            if y_prime > v:  # check the result line first
                continue
            # now loop in x
            for x in range(scaled_x):
                x_prime = float(x / SCALE)
                # if that point is inside a session then we mark a 1 on its ground
                if p.With(key).CheckPoint(x_prime, y_prime):
                    ground[y][x] = 1
    
    return ground


"""
this method will create the center of mass
with a given np array.
"""
def calculate(input):
    return ndimage.measurements.center_of_mass(input)
