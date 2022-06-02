from parameter import Parameter
"""
Testing our parameter class.
"""

t = Parameter().Range([0, 10, 5]).RightFunction(-1, 1).LeftValue(0).RightValue(0)
print(t.Info())

print(t.Input(12))  # expect 0
print(t.Input(-1))  # expect 0
print(t.Input(5))   # expect 5
print(t.Input(4))   # expect 4
print(t.Input(6))   # expect 4
