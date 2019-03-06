#when you override methods such as __iter__ and next() then that class becomes an iterator (2.7)

#iterator is a more general concept:
# any object whose class has a next method (__next__ in Python 3) and an __iter__ method
# that does return self


#Every generator is an iterator, but not vice versa. A generator is built by calling a
# function that has one or more yield expressions
class Squares(object):
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop
    def __iter__(self): return self
    def __next__(self):
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current

iterator = Squares(1, 6)
print(list(iterator))



#GENERATOR
def squares(start, stop):
    for i in range(start, stop):
        yield i * i

generator = squares(1, 6)
print(list(generator))

#OR

generator2 = (i*i for i in range(1, 6))
# print(list(generator2))
print(generator2.__next__())


#The __iter__ function is what is invoked when you attempt to use an object with a for-loop.
# Then __next__ or next is called on the iterator object to get each item out for the loop.
# The iterator raises StopIteration when you have exhausted it, and it cannot be reused at that point.

#for i in nlist:   nlist.iter().next()??Something like that
import collections

class Yes(collections.Iterator):
    def __init__(self, stop):
        self.x = 0
        self.stop = stop
    def __iter__(self):
        return self
    def next(self):
        if self.x < self.stop:
            self.x += 1
            return 'yes'
        else:
            # Iterators must raise when done, else considered broken
            raise StopIteration
    __next__ = next # Python 3 compatibility
stop = 5
yes_expr = ('yes' for _ in range(stop))
for i, y1, y2, y3 in zip(range(stop), Yes(stop), Yes(stop),('yes' for _ in range(stop))):
    print('{0}: {1} == {2} == {3}'.format(i, y1, y2, y3))





#Coroutines:

# yield forms an expression that allows data to be sent into the generator
# Here is an example, take note of the received variable, which
# will point to the data that is sent to the generator:

def bank_account(deposited, interest_rate):
    while True:
        calculated_interest = interest_rate * deposited
        print(calculated_interest)
        received = yield calculated_interest
        print(received)
        if received:
            print(deposited)
            deposited += received
            print(deposited)


my_account = bank_account(1000, .05)
print(type(my_account))
first_year_interest = next(my_account)

print(first_year_interest)

#And now we can send data into the generator. (Sending None is the same as calling next.) :
next_year_interest = my_account.send(first_year_interest + 1000)
print(next_year_interest)


# 2
# Python3 program for demonstrating
# coroutine execution

def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        print('Inside while')
        name = (yield)
        print('After yield',name)
        if prefix in name:
            print('inside IF')
            print(name)

        # calling coroutine, nothing will happen


corou = print_name("Dear")
print(type(corou))
# This will start execution of coroutine and
# Prints first line "Searchig prefix..."
# and advance execution to the first yield expression
corou.__next__()

# sending inputs
corou.send("Atul")
corou.send("Dear Atul")
corou.send("Dear Shivam")
corou.close()


# Python3 program for demonstrating
# coroutine chaining

def producer(sentence, next_coroutine):
    '''
    Producer which just split strings and
    feed it to pattern_filter coroutine
    '''
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    '''
    Search for pattern in received token
    and if pattern got matched, send it to
    print_token() coroutine for printing
    '''
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")


def print_token():
    '''
    Act as a sink, simply print the
    received tokens
    '''
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")


pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine=pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)