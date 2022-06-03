"""
Testing our expert fuzzy system.
"""

import simplejson
from fuzz import EFS

f = EFS()

f.NewParam('test').NewSession('test1').Range([0, 2, 1]).LeftValue(0).RightValue(0)
f.Param('test').NewSession('test2').Range([1, 3, 2]).LeftValue(0).RightValue(0)
print(simplejson.dumps(f.Info(), sort_keys=True, indent=4, use_decimal=True))

print(f.Param('test').Input(12))    # expect 0, 0
print(f.Param('test').Input(-1))    # expect 0, 0
print(f.Param('test').Input(1))     # expect 1, 0
print(f.Param('test').Input(0.5))   # expect 0.5, 0
print(f.Param('test').Input(1.5))   # expect 0.5, 0,5
