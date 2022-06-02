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
    def __init__(self):
        # parameter range
        self.range = [0, 0, 0]
        # parameter base functions
        self.lbf = dict(a=1, b=0)
        self.rbf = dict(a=1, b=0)
        # parameter range values
        self.rrv = 1
        self.lrv = 1

        return self
    
    def Range(self):
        return self
    
    def LeftFunction(self):
        return self

    def RightFunction(self):
        return self 

    def LeftValue(self):
        return self
    
    def RightValue(self):
        return self

    def Input(self, x):
        y = x

        return y
