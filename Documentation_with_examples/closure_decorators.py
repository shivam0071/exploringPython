# https://www.youtube.com/watch?v=VWZAh1QrqRE
# https://www.youtube.com/watch?v=_AEJHKGk9ns

# https://github.com/lord63/awesome-python-decorator -- SOME USE FULL builtin decorators

# CLOSURE : Sometimes we want a function to retain a value when it was created even though the
# scope cease to exist. This technique of using the values of outer parameters within a
# dynamic function is another way of defining the closure.
#
# the inner function remembers the environment in which it was created
# In other words, the inner function has access to the outer function’s variables and parameters.


# DECORATOR
# from functools import lru_cache
# lru_cache decorator stores the computation value and
# gives intant results when the function is called 2nd time onwards
# if more than one decorator is used then they are executed bottom to top

# Some Analysis :-
# Whenever we decorate a function with a decorator
# @new_func
# def func(n1,n2)
#
# then first new_func is called and the function func is implicitly passed so its kinda like
# new_func(func)
# Now if a wrapper(function inside a decorator) defined with in a decorator
# (which we usually should but not necessary) then that wrapper also automatically accepts
# the no of args that the originally function has
#
# basically it should return a function as it gets called automatically
# so we can return the function passed or the wrapper or even a lambda function
#
# checkout closure_decorator.py for decorators with args and class decorators
#
# Deco with args:-
# 1.)using  triple functions:
# the outermost function act as a decorator for a decorator and returns a decorator function lol
# which then acts like a normal decorator
# So when we say @outermost_Deco(args1,args2)
# this outermost gets called which returns a decorator ( the call is made without calling the normie
# function)
# now when the normie is called it behaves like how it should with a normal decorator

# Functions in python are first class objects -- can be passed as arguments and returned

# 1 CLOSURE Example
# A very simple but awesome closure,
# A function accepting a string (a function would make it decorator) and returning a function
import functools


def prefix_factory(prefix: str):
    def prefix_print(text: str):
        print(f"{prefix}: {text}")

    return prefix_print

debug = prefix_factory("DEBUG")
info = prefix_factory("INFO")
debug("This is debug log")
info("This is info log")


# 2 Decorator Example

def reverse_factory(func):
    def reverse_caller(text: str):
        func(text[::-1])

    return reverse_caller

factory1 = reverse_factory(debug)
factory1("String coming from Decorator")

factory2 = reverse_factory(info)
factory2("INFO LEVEL")

factory3 = reverse_factory(print)
factory3("Some string for print")

# Essentially we can just use @ on top of a function
@reverse_factory
def greet(name):
    print(f"Hi {name}")

greet("Shivam")

# 3 A more general decorator using * and **

# *, ** usage
def params(*args, **kwargs):
    print(f"{args = }")
    print(f"{kwargs = }")

params(12, 3, 4, 'demo', name='goku')

def reverse_factory(func):
    def reverse_caller(*args, **kwargs):
        func(*args, **kwargs)

    return reverse_caller

@reverse_factory
def greet(name):
    print(f"Hi {name}")

greet("Vegita")


# Exercise - 2

import random

def do_twice(func):
    def wrapper(*args, **kwargs):
        roll1 = func(*args, **kwargs)
        roll2 = func(*args, **kwargs)
        return (roll1, roll2)
    return wrapper

@do_twice
def roll_dice():
    return random.randint(1, 6)

print(roll_dice())

# Exercise - 3 -- Store whichever fucntions are decorated in a variable {"func_name": reference to it}

FUNCTIONS = {}
def register(func):
    func_name = func.__name__
    if func_name not in FUNCTIONS:
        FUNCTIONS.update({func_name: func})

    return func

@register
def roll_dice():
    return random.randint(1, 6)

@register
@do_twice
def roll_dice2():
    return random.randint(10, 20)


# register(do_twice(roll_dice2))
# do_twice returns a wrapper so the original name roll_dice2 is changed to wrapper...we can fix this by
# using functools.wraps which internally uses update_wrapper()
# {'roll_dice': <function roll_dice at 0x000002B3EF9EACA0>, 'wrapper': <function do_twice.<locals>.wrapper at 0x000002B3EF9EAAF0>}

# FIX
from functools import wraps
def do_twice(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        roll1 = func(*args, **kwargs)
        roll2 = func(*args, **kwargs)
        return (roll1, roll2)
    return wrapper

@register
@do_twice
def roll_dice3():
    return random.randint(10, 20)

# {'roll_dice3': <function roll_dice3 at 0x000002535CC1EF70>}
# print(dir(roll_dice3))
# '__wrapped__' has been added which points to the original function

print("************")
print(FUNCTIONS)
print(FUNCTIONS["roll_dice"]())
print(FUNCTIONS["roll_dice3"]())


# Exercise - 5 : make a retry decorator which make sure we can a 6 on a dice...original function is already written
def retry(func):
    @wraps(func)
    def wrapper():
        while True:
            try:
                return func()
            except ValueError as ve:
                print(f" Retrying {ve}")
    return wrapper

@register
@retry
def only_roll_sixes():
    number = random.randint(1, 6)
    if number != 6:
        raise ValueError(number)

    return number

print("************")
print(FUNCTIONS)
print(only_roll_sixes())

#  TENACITY library has similar functionality plus other features

#  EXAMPLE - 6 (HARD) : PARAMETERIZED DECORATOR, rewrite retry so that it only retries on specific, user defined exceptions

def retry(*exceptions):
    def outer_wrap(func):
        def inner_wrap():
            while True:
                try:
                    return func()
                except exceptions as ex:
                    print(f"Retrying {ex}")
        return inner_wrap
    return outer_wrap


@retry(ValueError, ZeroDivisionError)
def calculation():
    number = random.randint(-5, 5)
    if abs(1 / number) > 0.2:
        raise ValueError(number)
    return number

# Its like
# retry(*args)(calculation)
print(calculation())


# Exercise - 7 add max_retries in decorator argument

def retry(max_tries=10):
    def outer_wrap(func):
        def inner_wrap():
            for _ in range(max_tries):
                try:
                    return func()
                except Exception as ex:
                    print(f"Retrying {ex}")
            print(f"Exceded Max Retries {max_tries}")
            return None

        return inner_wrap
    return outer_wrap


@retry(max_tries=20)
def calculation():
    number = random.randint(-5, 5)
    if abs(1 / number) > 0.2:
        raise ValueError(number)
    return number

# Its like
# retry(*args)(calculation)
print("*****************")
print(calculation())

#  We can also save a decorators STATE by

def retry(max_tries=10):
    def outer_wrap(func):
        def inner_wrap():
            for _ in range(max_tries - inner_wrap.max_trie):
                try:
                    return func()
                except Exception as ex:
                    print(f"Retrying {ex}")
                    inner_wrap.max_trie += 1
            print(f"Exceded Max Retries {max_tries}")
            return None
        inner_wrap.max_trie = 0
        return inner_wrap
    return outer_wrap

@retry(max_tries=15)
def calculation():
    number = random.randint(-5, 5)
    if abs(1 / number) > 0.2:
        raise ValueError(number)
    return number

print(f"TRIES {calculation.max_trie}")
calculation()
print(f"TRIES Used {calculation.max_trie}")
print("***************")
calculation()
print(f"TRIES Used {calculation.max_trie}")


# Exercise - FINAL ... do the above using Class Decorators

class Retry():

    track = 0
    def __init__(self, max_tries):
        self.max_tries = max_tries


    def __call__(self, func):
        @functools.wraps(func)
        def wrapper():
            for _ in range(self.max_tries - Retry.track):
                try:
                    return func()
                except Exception as ex:
                    print(f"Retrying {ex}")
                    Retry.track += 1
            print("Track limit exceeded")
        return wrapper


@Retry(max_tries=8)
def calculation():
    number = random.randint(-5, 5)
    if abs(1 / number) > 0.2:
        raise ValueError(number)
    return number

print("***************")
print("***************")
print(calculation)
print(f"TRIES Used {Retry.track}")
calculation()
print(f"TRIES Used {Retry.track}")
print("***************")
calculation()
print(f"TRIES Used {Retry.track}")