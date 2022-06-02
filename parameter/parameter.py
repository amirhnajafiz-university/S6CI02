from decimal import Decimal


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

        self.LeftFunction(lin_equ((self.range[0], 0), (self.range[2], 1)))
        self.RightFunction(lin_equ((self.range[2], 1), (self.range[1], 0)))

        return self
    
    def LeftFunction(self, value):  # setting the left function parameters
        self.lbf.update(dict(a=value[0], b=value[1]))

        return self

    def RightFunction(self, value):  # setting the right function parameters
        self.rbf.update(dict(a=value[0], b=value[1]))

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
            return self.lbf.get('a') * Decimal(x) + self.lbf.get('b')
        elif x >= self.range[2] and x < self.range[1]:  # middle right
            return self.rbf.get('a') * Decimal(x) + self.rbf.get('b')
        elif x >= self.range[1]:  # right
            return self.rrv

    def Info(self):
        return dict(
            Range=self.range,
            LeftBaseFunction=self.lbf,
            RightBaseFunction=self.rbf,
            LeftRangeValue=self.lrv,
            RightRangeValue=self.rrv
        )


def lin_equ(l1, l2):  # calculating the line from two points
    m = Decimal((l2[1] - l1[1])) / Decimal(l2[0] - l1[0])
    c = (l2[1] - (m * l2[0]))
    return m, c
