"""
Testing our parameter class.
"""

import simplejson
from parameter import Parameter


t = Parameter().Range([0, 2, 1]).LeftValue(0).RightValue(0)
print(simplejson.dumps(t.Info(), sort_keys=True, indent=4, use_decimal=True))

print(t.Input(12) == 0)    # expect 0
print(t.Input(-1) == 0)    # expect 0
print(t.Input(1) == 1)     # expect 1
print(t.Input(0.5) == 0.5)   # expect 0.5
print(t.Input(1.5) == 0.5)   # expect 0.5
