"""
Parameter class.
    - fields:
        - range: type list [begin, end, middle]
        - base function left (a, b)
        - base function right (a , b)
        - right range value
        - left range value

"""
class Parameter:
    def __init__(self):  # constructor
        # parameter range
        self.range = [0, 0, 0]
        # parameter base functions
        self.lbf = dict(a=1, b=0)
        self.rbf = dict(a=1, b=0)
        # parameter range values
        self.rrv = 1
        self.lrv = 1
    
    def Range(self, newRange):  # setting the parameter range
        self.range = newRange

        return self
    
    def LeftFunction(self, a, b):  # setting the left function parameters
        self.lbf.a = a
        self.lbf.b = b

        return self

    def RightFunction(self, a, b):  # setting the right function parameters
        self.rbf.a = a
        self.rbf.b = b

        return self 

    def LeftValue(self, value):  # setting the left value range
        self.lrv = value

        return self
    
    def RightValue(self, value):  # setting the right value range
        self.rrv = value

        return self

    def Input(self, x):  # calculating the output of parameter
        if x <= self.range[0]:  # left 
            return self.lrv
        elif x > self.range[0] and x < self.range[2]:  # middle left
            return self.lbf.a * x + self.lbf.b
        elif x >= self.range[2] and x < self.range[1]:  # middle right
            return self.rbf.a * x + self.rbf.b
        elif x >= self.range[1]:  # right
            return self.rrv
