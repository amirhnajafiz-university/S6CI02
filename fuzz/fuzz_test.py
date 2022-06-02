"""
Testing our expert fuzzy system.
"""


from fuzz import EFS

f = EFS()

f.NewParam('test').Range([0, 2, 1]).LeftValue(0).RightValue(0)
print(f.Info())

print(f.Param('test').Input(12) == 0)    # expect 0
print(f.Param('test').Input(-1) == 0)    # expect 0
print(f.Param('test').Input(1) == 1)     # expect 1
print(f.Param('test').Input(0.5) == 0.5)   # expect 0.5
print(f.Param('test').Input(1.5) == 0.5)   # expect 0.5