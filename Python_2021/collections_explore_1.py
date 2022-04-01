# https://docs.python.org/3/library/collections.html

# 1.) CHAIN MAP
# A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit.
# It is often much faster than creating a new dictionary and running multiple update() calls.

from collections import ChainMap

baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
print(list(ChainMap(adjustments, baseline)))

# 2.) Counter
# 3.) Deque
# 4.) defaultdict
# 5.) namedtuple
# 6.) ordereddict
