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
