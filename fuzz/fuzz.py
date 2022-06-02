from parameter import Parameter


"""
Expert fuzzy system class.
    - this class has parameters that each parameter has a range and
    a function.
    - you can add parameters with name.
        - for each parameter, you can set a range.
        - for each parameter, you can set 2 base functions.
        - for each parameter, you can set 2 out of range values for left and right.
    - you can remove parameters.
"""
class EFS:
    def __init__(self):  # constructor
        # create the dict of parameters
        self.parameters = {}
    
    def NewParam(self, name):  # adding a new parameter
        p = Parameter()
        self.parameters[name] = p

        return p
    
    def DelParam(self, name):  # removing parameters
        self.parameters.pop(name)

    def Param(self, name):  # choosing parameters
        for i in parameters.keys():
            if i == name:
                return self.parameters.get(name)
        return NULL

    def Info(self):  # EFS information
        return dict(
            Length=len(self.parameters),
            Parameters=self.parameters
        )
