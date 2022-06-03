from parameter.parameter import Parameter
from scipy import ndimage
import numpy as np


# our output parameter
output = Parameter()
output.NewSession('healthy').Range([0.25, 1, 0.25]).LeftValue(1)
output.NewSession('sick1').Range([0, 2, 1])
output.NewSession('sick2').Range([1, 3, 2])
output.NewSession('sick3').Range([2, 4, 3])
output.NewSession('sick4').Range([3, 3.75, 3.75]).RightValue(1)


def calculate(input):
    masses = np.array(
        [
            [0,  0,  0,  0],
            [0,  1,  0,  0],
            [0,  2,  0,  0],
            [1,  0,  0,  0],
            [1,  1,  0,  1],
            [1,  2,  0,  1],
            [2,  0,  0,  0],
            [2,  1,  0,  0],
            [2,  2,  0,  0]
        ]
    )

    print(ndimage.measurements.center_of_mass(masses))


def defuzzify(input):
    # get the results and create the output
    pass
