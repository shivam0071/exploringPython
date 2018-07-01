#1 July 2018
#12:14 PM

# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
#A metaclass is the class of a class. Like a class defines how an instance of the class behaves,
#  a metaclass defines how a class behaves. A class is an instance of a metaclass.
# Metaclass in python :-
# type(name, bases, dict) --> a new type
#
# so a Metaclasses take 3 args. 'name', 'bases' and 'dict'
# where
# name is the name of the class
# bases is the args passed -- ()
# while dict is all the class variable and functions used -- {}

# example for python 2
# def test_metaclass(name, bases, dict):
#     print('The Class Name is', name)
#     print('The Class Bases are', bases)
#     print('The dict has', len(dict), 'elems, the keys are', dict.keys())
#
#     return "yellow"
#
# class TestName2(object, None, int, 1):
#     __metaclass__ = test_metaclass
#     foo = 1
#     def baz(self, arr):
#         pass
#
# print ('TestName = ', repr(TestName2))


# the metaclass will automatically get passed the same argument
# that you usually pass to `type`
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
      Return a class object, with the list of its attribute turned
      into uppercase.
    """

    # pick up any attribute that doesn't start with '__' and uppercase it
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # this will affect all classes in the module

class Foo(): # global __metaclass__ won't work with "object" though
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    bar = 'bip'

print(hasattr(Foo, 'bar'))
# Out: False
print(hasattr(Foo, 'BAR'))
# Out: True

f = Foo()
# print(f.BAR)
# Out: 'bip'