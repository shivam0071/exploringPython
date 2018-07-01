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
    @wraps(func)   #Keeps data about the function..such as name and docs...without it...it returns wrapper
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def countdown(n: int):   # Modified ...it accepts any arg and kwarg now,
                         # Here n: int is an annotation earlier countdown(n) only
    '''
    countdown function
    '''
    while n > 0:
        n -= 1

if __name__ == '__main__':
    #if no decorator was used about countdown then we would do this:
    # countdown = timethis(countdown)
    countdown(1000000)


    c = countdown
    c(1000000)
    print(c.__name__, c.__doc__, c.__annotations__)  #name is wrapper without wraps and doce is none




    #An important feature of the @wraps decorator is that it makes the wrapped function
    # available to you in the __wrapped__ attribute. For example, if you want to access the
    # wrapped function directly
    print(countdown.__wrapped__(100000), 'Here')

    #The decorator keeps the return type same as that of the function

    #The presence of the __wrapped__ attribute also makes decorated functions properly
    # expose the underlying signature of the wrapped function
    from inspect import signature
    print('Signature - ',signature(countdown))


#Unwrapping a Decorator
# Problem
# A decorator has been applied to a function, but you want to “undo” it, gaining access to
# the original unwrapped function.

