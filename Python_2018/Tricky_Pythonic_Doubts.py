# https://docs.python.org/3/faq/programming.html#general-questions

# Why do lambdas defined in a loop with different values all return the same result?

squares = []
for x in range(5):
    squares.append(lambda: x**2)


print(squares[0]())

# 16
# This happens because x is not local to the lambdas,
# but is defined in the outer scope, and it is accessed when the lambda is called —
# not when it is defined. At the end of the loop, the value of x is 4, so all the
# functions now return 4**2, i.e. 16. You can also verify this by changing the value of
# x and see how the results of the lambdas change:

x = 8
print(squares[0]())

# In order to avoid this, you need to save the values in variables local to the lambdas,
# so that they don’t rely on the value of the global x:

squares2 = []
for x in range(5):
    squares2.append(lambda n=x: n**2)

print (squares2[0](),squares2[1](),squares2[2](),squares2[3](),squares2[4]())


# How do you make a higher order function in Python?
# suppose you wanted to define linear(a,b) which returns a function f(x) that
# computes the value a*x+b. Using nested scopes:
def linear(a, b):
    def result(x):
        return a * x + b
    return result


# The callable object approach has the disadvantage that it is a bit slower and
#  results in slightly longer code. However, note that a collection of callables can share their signature via inheritance:
class linear:

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __call__(self, x):
        return self.a * x + self.b

class counter:

    value = 0

    def set(self, x):
        self.value = x

    def up(self):
        self.value = self.value + 1

    def down(self):
        self.value = self.value - 1

count = counter()
inc, dec, reset = count.up, count.down, count.set

# Deep Copy and Shallow Copy

import copy
a = 'Shaan'
ls = [1,2,[33,44,55],a,5]
newls = copy.copy(ls)
deepls = copy.deepcopy(ls)
print(newls)
print(deepls)
# The difference between shallow and deep copying is only relevant for
# compound objects (objects that contain other objects, like lists or class instances):
#
# A shallow copy constructs a new compound object and then (to the extent possible)
# inserts references into it to the objects found in the original.
# A deep copy constructs a new compound object and then, recursively,
# inserts copies into it of the objects found in the original.

# How do I use strings to call functions/methods?

def a():
    pass

def b():
    pass

dispatch = {'go': a, 'stop': b}  # Note lack of parens for funcs

dispatch['go']()  # Note trailing parens to call function

# class Foo:
#     def do_foo(self):
#         ...
#
#     def do_bar(self):
#         ...
#
# f = getattr(foo_instance, 'do_' + opname)
# f()