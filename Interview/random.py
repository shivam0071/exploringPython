#1 count the no of function calls using a decorator

def counter1(funct):
  funct.counter = 0
  def wrapper():
    funct.counter += 1
    funct()
    print('i am being called for the ', funct.counter, ' times')
  return wrapper

@counter1
def function1():
  print('I am function 1')

@counter1
def function2():
  print('I am function 2')

# function1()
# function1()
# function2()
# function1()
# function2()
# function1()


# 2.) THREADING

import threading
import time

def count(n):
  while n > 0:
    n-=1

n = 50000000

# start = time.time()
# count(n)
# count(n)
# count(n)
# count(n)
# end = time.time()
# print('Time take by a main threaded program', end-start)
#  8.312624454498291
# 16.152875661849976 for twice
# 32.02449822425842 for 4 times

# start = time.time()
# t1 = threading.Thread(target=count, args=(n,))
# t2 = threading.Thread(target=count, args=(n,))
# t3 = threading.Thread(target=count, args=(n,))
# t4 = threading.Thread(target=count, args=(n,))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# end = time.time()
# print('Time take by a t1 thread', end-start)
# # Single threaad t1 7.879119157791138
# 15.184135913848877 for twice
# 30.59863829612732 4 threads



from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
  start = time.time()
  p1 =Process(group=None, target=count, args=(n,))
  p2 =Process(group=None, target=count,args=(n,))
  p3 = Process(group=None, target=count, args=(n,))
  p4 = Process(group=None, target=count, args=(n,))
  p1.start()
  p2.start()
  p3.start()
  p4.start()
  p1.join()
  p2.join()
  p3.join()
  p4.join()
  end = time.time()
  print('Time take by a processs', end-start)
  # 9.562638998031616 2 processes
  # 18.23465871810913 4 processes WOAH