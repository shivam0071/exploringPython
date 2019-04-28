# 06/03/2019
# Here we are going to implement special methods which have BIFs namely
# + * abs()
from math import hypot
class Vector:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    '''For String representation of the object'''
    return 'Vector(%r, %r)' % (self.x, self.y) # here r is for repr ( {!r}.format()

  def __abs__(self):
    '''the distance from 0 (pythagoras theorem) original
    abs() accepts just one arg and this too but it takes a vector and
    finds abs for x and y'''
    return hypot(self.x, self.y)

  def __bool__(self):
    return bool(abs(self))

  def __add__(self, other):
    '''uses  + '''
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)

  def __mul__(self, scalar):
    '''uses * (multiply vector by a number and not a number by a vector'''
    return Vector(self.x * scalar, self.y * scalar)

v = Vector(10,20)
print(v, abs(v), v + Vector(22,22), v * 10, bool(Vector(0,0)))



# the length is
# simply read from a field in a C struct. Getting the number of items in a collection is a
# common operation and must work efficiently for such basic and diverse types as str,
# list, memoryview etc.

# Further Read
# https://docs.python.org/3/reference/datamodel.html

# page - 19
