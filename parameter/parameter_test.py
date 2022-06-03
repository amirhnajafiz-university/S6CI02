"""
Testing our parameter class.
"""


import simplejson
from parameter import Parameter

p = Parameter()

p.NewSession('test').Range([0, 2, 1]).LeftValue(0).RightValue(0)
print(simplejson.dumps(p.Info(), sort_keys=True, indent=4, use_decimal=True))

print(p.With('test').Input(12) == 0)    # expect 0
print(p.With('test').Input(-1) == 0)    # expect 0
print(p.With('test').Input(1) == 1)     # expect 1
print(p.With('test').Input(0.5) == 0.5)   # expect 0.5
print(p.With('test').Input(1.5) == 0.5)   # expect 0.5
