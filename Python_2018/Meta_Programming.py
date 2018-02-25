# any time you are faced with a problem of creating highly repetitive code (or
# cutting or pasting source code), it often pays to look for a more elegant solution. In
# Python, such problems are often solved under the category of “metaprogramming.”


# metaprogramming is about creating functions and classes whose main goal
# is to manipulate code (e.g., modifying, generating, or wrapping existing code). The main
# features for this include decorators, class decorators, and metaclasses

# 1 .Putting a Wrapper Around a Function
# Problem :
# You want to put a wrapper layer around a function that adds extra processing (e.g.,
# logging, timing, etc.).


# SOLUTION :- The functools module is for higher-order functions: functions that act on or return other functions.
#  In general, any callable object can be treated as a function for the purposes of this module.


# functools.wraps. This takes a function used in a decorator and adds the
#  functionality of copying over the function name,
#  docstring, arguments list, etc. And since wraps is itself a decorator,
#  the following code does the correct thing:

# from functools import wraps
# def logged(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print func.__name__ + " was called"
#         return func(*args, **kwargs)
#     return with_logging
#
# @logged
# def f(x):
#    """does some math"""
#    return x + x * x
# print f.__name__  # prints 'f'  ... Without @wrap it would print with_logging
# print f.__doc__   # prints 'does some math'  ...no doc string would have been printed without wraps


import time
from functools import wraps
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def countdown(n):   #Modified ...it accepts any arg and kwarg now
    '''
    countdown
    '''
    while n > 0:
        n -= 1

countdown(1000000)

#The decorator keeps the return type same as that of the function