# https://www.youtube.com/watch?v=EnSu9hHGq5o

# Both Iterators and Generators does lazy evaluation
# Generators are easier to write and read using yield
# Iterable - Stream of data >  lists, dictionaries, sets, frozen sets, strings, byte strings, byte arrays, ranges and memory views:
# Iterator - Iterators require a next or __next__ method
# The __iter__ method is called when you attempt to use an object with a for-loop.
# Then the __next__ method is called on the iterator object to get each item out for the loop.
# The iterator raises StopIteration when you have exhausted it, and it cannot be reused at that point.

# If Iteratable is a book then Iterator is a bookmark.

# A generator is a coroutine...It interleaves user code and library code by using yield (giving control)
# user asks generator for a value (control goes to gen) it gives user a value (back to user) and so on
# so when you need one value at a time & compute on it (without storing), use a generator

# Generators can also be used to enforce sequencing..calling some functions in sequence only one after the other
# https://www.youtube.com/watch?v=7lmCu8wz8ro&list=LL&index=3&t=2145s

# 1 A Simple Iterator by overriding __iter__
class Tasks:

    def __init__(self):
        self.task = ['task 1', 'task 2']

    def __iter__(self):
        return iter(self.task)

for task in Tasks():
    print(task)

# 2 A simple generator by overriding __iter__

class Tasks2:

    def __init__(self):
        self.task = ['yield task 1', 'yield task 2']

    def __iter__(self):
        # If this is the best place to create an Iterator then it can also be used to create a generator
        for task in self.task:
            # Some Filtering on task
            yield task

    # Iterator
    def all(self):
        # iterate over all tasks
        return iter(self.task)

for task in Tasks2():
    print(task)


# GENERATORS and ITERATORS best practice and WHY to use them

# When we are looping over a stream of data (list) then
# Avoid using Indexes is python....there is a simpler way
# Try to use generators(yield and __iter__) as much as possible, Why ?
    # they does lazy evaluation,
    # We can run over a huge data without any memory burden. eg. reading files, huge dataset
# Try to abstract the logic of looping over stream of data and use yield


# 3 Using Abstractions and Yields
# FIND EVEN NUMBER

# Normal Code
def do_something(data):
    # Some computation with the data
    print(data)

def compute_even(ls):
    for data in ls:
        # imagine if the filters are quite complex and a lot of them...why not abstract that code
        if data % 2 == 0:
            do_something(data)
ls = [33, 44, 55, 1, 2 ,3, 77, 88, 99]
compute_even(ls)


# 4 Abstraction and Yield - This can be replaced
# Abstracting the complexity, doing whats needed...can also resolve breaking from a nested for loops
def find_even(ls):
    for data in ls:
        if data % 2 == 0:
            yield data

def compute_even2(ls):
    for data in find_even(ls):
        do_something(data)

compute_even2(ls)


# 5 BASIC ITERATOR - STOP ITERATION

class Tasks:

    def __init__(self, stop):
        self.x = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.x < self.stop:
            self.x += 1
            return self.x - 1
        else:
            # Iterators must raise when done, else considered broken
            raise StopIteration

for task in Tasks(10):
    print(task)

#6 Same thing using YIELD
def task_yield(stop):
    print("*************************")
    for data in range(stop):
        yield data

for data in task_yield(10):
    print(data)


#  7 EXTRAS
# Generators are objects that allow us to suspend the execution of a python function.
# User curated generators are implement using the keyword yield.
# By creating a normal function containing the yield keyword,
# we turn that function into a generator:


# A less-known feature of generators, is the fact that you can communicate with them using two methods:
# send() and throw().

def simple_gen():
    yield 1
    yield 2


# Communicating with a generator
def simple_gen_2():
    val1 = yield "YO"
    print(val1)
    yield 2
    yield 3

# Returning values from generators
def simple_gen3():
    yield "Hello"
    return "World"


#  YIELD FROM
# What that keyword allows us to do, is pass on any next(), send() and throw() into an inner-most nested generator.
# If the inner generator returns a value, it is also the return value of yield from

# Upon introducing the new keyword yield from in Python 3.4, we were now able to create generators inside generators
# that just like a tunnel, pass the data back and forth from the inner-most to the outer-most generators.
# This has spawned a new meaning for generators - coroutines.
def inner():
    inner_result = yield 2
    print('inner', inner_result)
    return 3

def outer():
    yield 1
    val = yield from inner()
    print('outer', val)
    yield 4

# Coroutines are functions that can be stopped and resumed while being run.
# In Python, they are defined using the async def keyword. Much like generators,
# they too use their own form of yield from which is await.
# Before async and await were introduced in Python 3.5, we created coroutines in the exact same way generators were created
# (with yield from instead of await).


async def inner2():
    return 1

async def outer2():
    await inner()



if __name__ == "__main__":
    gen = simple_gen()
    print(next(gen))
    print(next(gen))
    # print(next(gen))      # Exception

    gen2 = simple_gen_2()
    print(next(gen2))
    print(gen2.send("abc"))
    # the value is passed as a return value from the yield keyword.
    print(next(gen2))
    # print(gen2.throw(Exception())) # Throws an exception
    # allows throwing Exceptions inside generators, with the exception raised at the same spot yield was called.


    gen3 = simple_gen3()
    print(next(gen3))
    # print(next(gen3))
    # Returning a value from a generator, results in the value being put inside the StopIteration exception.
    # We can later on recover the value from the exception and use it to our need.
    # Traceback (most recent call last):
    #   File "D:\Code\exploringPython\Python_2021\the_generators_secret.py", line 45, in <module>
    #     print(next(gen3))
    # StopIteration: World
    try:
        print(next(gen3))
    except Exception as ex:
        print(ex.value)


    print("********************")
    gen4 = outer()
    print(next(gen4))
    print(next(gen4))
    print(gen4.send("aabbcc"))
    # print(next(gen4))


    # asio = outer2()
