from scipy import ndimage
import numpy as np

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
