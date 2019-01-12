# Returns a new dictionary-like object. defaultdict is a subclass of
# the built-in dict class. It overrides one method and adds one writable instance variable.
from collections import defaultdict
import random
import string

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# here we create a dict but the values of dictionaries can be of the type list,string,tuple,int etc
d = defaultdict(list)
# gives defaultdict(<class 'list'>, {})
print(d)

for k, v in s:
  d[k].append(v)

# d[k] retuns an empty list as there are no element wiht that key
# (empty ist added to the default dict with key k)
# now when the empty list is return we are just appending elements to it
print(d)
# defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})

def random_dictionary_generator(n,m):
  def random_name(m):
    ke = ''.join([string.ascii_letters[random.randint(0, 51)] for i in range(m)])
    return ke,ke[::-1]

  return dict([random_name(m)for i in range(n)])


print(random_dictionary_generator(5,6))