

# https://docs.python.org/3/tutorial/classes.html#private-variables
# PRIVATE VARIABLES
class under_scores():

  def __init__(self):
    self._semiprivate =  10
    self.__superprivate = 20

us = under_scores()
print(us._semiprivate)
# print(us.__superprivate)


# NAMED TUPLES
# Returns a new tuple subclass named typename. The new subclass is used to create
# tuple-like objects that have fields accessible by attribute lookup as well as be
# ing indexable and iterable. Instances of the subclass also have a helpful docstr
# ing (with typename and field_names) and a helpful __repr__() method which lists
# the tuple contents in a name=value format.
import collections
Student = collections.namedtuple('Student',['name','age','DOB'])
S = Student('Nandini','19','2541997')
# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))

# SPECIAL METHOD NAMES
# string/bytes representation :-  __repr__, __str__, __format__, __bytes__
# conversion to number :- __abs__, __bool__, __complex__, __int__, __float__, __hash__, __in
# dex__
# emulating collections :-  __len__, __getitem__, __setitem__, __delitem__, __contains__
# iteration :- __iter__, __reversed__, __next__
# emulating callables :- __call__
# context management :- __enter__, __exit__
# instance creation and destruction  :- __new__, __init__, __del__
# attribute management :- __getattr__, __getattribute__, __setattr__, __delattr__, __dir__
# attribute descriptors :- __get__, __set__, __delete__
# class services :- __prepare__, __instancecheck__, __subclasscheck__

