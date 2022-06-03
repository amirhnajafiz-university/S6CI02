from parameter.parameter import Parameter
from scipy import ndimage
import numpy as np
from decimal import Decimal

# scales
SCALE = 1000
# limits
LIMIT_Y = 0.1
LIMIT_X = 4


# our output parameter
output = Parameter()
output.NewSession('healthy').Range([0.25, 1, 0.25]).LeftValue(1)
output.NewSession('sick_1').Range([0, 2, 1])
output.NewSession('sick_2').Range([1, 3, 2])
output.NewSession('sick_3').Range([2, 4, 3])
output.NewSession('sick_4').Range([3, 3.75, 3.75]).RightValue(1)


def defuzzify(input):
    y, x = calculate(initialize(input))
    return float(x / SCALE)


def initialize(values):
    mx = int(LIMIT_X*SCALE)
    my = int(LIMIT_Y*SCALE)

    ground = np.zeros((my, mx))
    for key in values.keys():
        r = output.With(key).GetRange()
        rf = output.With(key).GetRightFunction()
        lf = output.With(key).GetLeftFunction()
        v = values.get(key)
        
        for yp in range(my):
            y = float(yp / SCALE)
            for xp in range(mx):
                x = float(xp / SCALE)

                if y > v or (x < r[0] or x > r[1]):
                    continue

                t1 = rf.get('a') * Decimal(x) + rf.get('b')
                t2 = lf.get('a') * Decimal(x) + lf.get('b')

                if y < t1 and x < r[2]:
                    ground[yp][xp] = 1
                elif y < t2 and x > r[2]:
                    ground[yp][xp] = 1
    
    return ground


def calculate(input):
    return ndimage.measurements.center_of_mass(input)
