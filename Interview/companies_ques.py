# Fid Int

# 1.) What is mutable and immutable in Python and is hashing and immutable same?

# 2. ) How to use Unix pipes input, output and error in python subprocess

# 3. ) list -- how to copy a list  = [1,2,3,[4,5,6]]
print('Question 1')
ls = [1,2,3,4,[5,6,7]]
ls2 = ls[:] # ls.copy()
ls[0] = 999
ls2[4][0] = 88
print(ls)
print(ls2)

# This was my answer which created a copy of the original
# list but couldn't copy the inner list

# But i predicted this output and answerd deep copy and shallow copy
from copy import deepcopy
del ls, ls2
print('Solution 1')
ls = [1,2,3,4,[5,6,7]]
ls2  = deepcopy(ls)
ls2[4][0] = 88
print(ls)
print(ls2)


# 4.) If tuple is immutable then explain this behaviour and output
print('Question 4')
t1 = (1,2,3,[4,5,6])
print(t1)
t1[3][0] = 222
print(t1)


# I predicted the output correctly and said the tuple is still immutable
# even though the list is changing...
# REASON

# An object is hashable if it has a hash value which never changes during its life
# time (it needs a __hash__() method), and can be compared to other objects (it ne
# eds an __eq__() or __cmp__() method). Hashable objects which compare equal must
# have the same hash value.

# Hashability makes an object usable as a dictionary key and a set member, because
#  these data structures use the hash value internally.

# So we can say
print('Solution')
t2 = (1,1,2,3,[4,5,6])
# print(t2.__hash__())
# print()
# t2[3][0] = 222
# print(t2.__hash__())

# DETAILS
# All Python objects have three things: a value, a type, and an identity. This is
# a bit confusing, because we often casually say, for example, "the value 42", alt
# hough 42 is also called an object which itself has a value

# >>> spam = 42
# >>> spam
# 42
# >>> type(spam)
# <class 'int'>
# >>> id(spam)
# 159428736

# The variable spam refers to an object that has a value of 42, a type of int, and
#  an identity of 1594282736. An identity is a unique integer, created when the ob
# ject is created, and never changes for the lifetime of the object. An object's t
# ype also cannot change. Only the value of an object may change

# More in PythonTutorial and Tips.txt

# 5.  Create a class in which ID increases with each new object created and
# printing an object gives some important info
print('Question 5')
class Emp():
  ID = 0
  def __init__(self, name):
    self.name = name
    Emp.ID += 1
    self.id = Emp.ID

  def __str__(self):
    return 'Name -> {}\nID->{}'.format(self.name, self.id)

a2 = Emp('Shivam')
b = Emp('Sookh')
print(a2)
print(b)

