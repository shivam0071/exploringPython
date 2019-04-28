from threading import Thread
import threading as th
from multiprocessing import Process
import time

def task(n):
  while n > 0:
    n -= 1


def time_taken(name):
  def wrap(fun):
    def wrapper(n):
      print('Running', name)
      start = time.time()
      fun(n)
      end = time.time()
      print('Time taken by '+name,end-start)
    return wrapper
  return wrap

# def threading_info(func):
#   # def wrapper(w):
#   # return wrapper
#     return lambda x: print('Heya',x)
#   #   return func

@time_taken('Thread')
def threading_pace(n):
  t1 = Thread(target=task,args=(n,))
  t2 = Thread(target=task,args=(n,))
  t3 = Thread(target=task, args=(n,))
  t4 = Thread(target=task, args=(n,))
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t1.join()
  t2.join()
  t3.join()
  t4.join()

@time_taken('Process')
def process_pace(n):
  p1 = Process(target=task,args=(n,))
  p2 = Process(target=task,args=(n,))
  p3 = Process(target=task,args=(n,))
  p4 = Process(target=task,args=(n,))

  p1.start()
  p2.start()
  p3.start()
  p4.start()
  p1.join()
  p2.join()
  p3.join()
  p4.join()



if __name__ == '__main__':
  num = 50000000
  # threading_pace(num)
  process_pace(num)
  print('MAIN')

  # print(threading_info())