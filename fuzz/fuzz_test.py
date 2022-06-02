"""
Testing our expert fuzzy system.
"""

import simplejson
from fuzz import EFS

f = EFS()

f.NewParam('test').Range([0, 2, 1]).LeftValue(0).RightValue(0)
print(simplejson.dumps(f.Info(), sort_keys=True, indent=4, use_decimal=True))

print(f.Param('test').Input(12) == 0)    # expect 0
print(f.Param('test').Input(-1) == 0)    # expect 0
print(f.Param('test').Input(1) == 1)     # expect 1
print(f.Param('test').Input(0.5) == 0.5)   # expect 0.5
print(f.Param('test').Input(1.5) == 0.5)   # expect 0.5