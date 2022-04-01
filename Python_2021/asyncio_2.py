# https://docs.python.org/3/library/asyncio.html
# https://docs.python.org/3.5/library/asyncio-task.html#example-chain-coroutines

# asyncio is a library to write concurrent code using the async/await syntax.
# asyncio is often a perfect fit for IO-bound and high-level structured network code.

import asyncio
import time

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')
#
# # Python 3.7+
# asyncio.run(main())


# import asyncio
# import time
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
# asyncio.run(main())

# The asyncio.create_task() function to run coroutines concurrently as asyncio Tasks.

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


# Awaitables
# We say that an object is an awaitable object if it can be used in an await expression.
# Many asyncio APIs are designed to accept awaitables.
#
# There are three main types of awaitable objects: coroutines, Tasks, and Futures.

# Coroutines
#
# Python coroutines are awaitables and therefore can be awaited from other coroutines:


async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # RuntimeWarning: coroutine 'nested' was never awaited
    # nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())
print("END")
#
# Important In this documentation the term “coroutine” can be used for two closely related concepts:
# a coroutine function: an async def function;
#
# a coroutine object: an object returned by calling a coroutine function.


# Tasks
#
# Tasks are used to schedule coroutines concurrently.
# When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon:

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())


# Running Tasks Concurrently
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())