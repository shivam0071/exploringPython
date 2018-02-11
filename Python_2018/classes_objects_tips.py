#11th Feb 2018 6.00 PM
# Changing the String Representation of Instances

#Teaches -> using in built functions (BIFs) __str__ and __repr__

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

# The __repr__() method returns the code representation of an instance, and is usually
# the text you would type to re-create the instance

# The __str__()
# method converts the instance to a string, and is the output produced by the str() and
# print() functions

# the special !r formatting code indicates that the
# output of __repr__() should be used instead of __str__(), the default.

if __name__ == '__main__':
    p = Pair(44, 'Shivam')
    print(p)
    print(p.__repr__())  # type p only in python console
