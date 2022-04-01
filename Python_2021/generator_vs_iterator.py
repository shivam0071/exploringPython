# A Generator IS A ITERATOR
# Both Iterators and Generators does lazy evaluation

import collections, types
print(issubclass(types.GeneratorType, collections.Iterator))
print(isinstance((i for i in range(0)), collections.Iterator))

# An Iterator IS A Iterable
print(issubclass(collections.Iterator, collections.Iterable))

# Some examples of iterables are the built-in tuples, lists, dictionaries, sets, frozen sets,
# strings, byte strings, byte arrays, ranges and memory views:

# Iterators require a next or __next__ method
# The __iter__ method is called when you attempt to use an object with a for-loop.
# Then the __next__ method is called on the iterator object to get each item out for the loop.
# The iterator raises StopIteration when you have exhausted it, and it cannot be reused at that point.


class Yes:

    def __init__(self, stop):
        self.x = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.x < self.stop:
            self.x += 1
            return 'yes'
        else:
            # Iterators must raise when done, else considered broken
            raise StopIteration

yes = Yes(5)
print(yes)
# <__main__.Yes object at 0x00000148EA7704C0>
print(isinstance(yes, collections.Iterator))
print([i for i in yes])

def yes2(stop):
    for _ in range(stop):
        yield 'yes'

gen_yes =  yes2(5)
print(gen_yes)
# <generator object yes2 at 0x00000148EA7D23C0>
print([d for d in gen_yes])