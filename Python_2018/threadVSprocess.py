from threading import Thread
import threading as th
from multiprocessing import Process
import time

def task(n):
  while n > 0:
    n -= 1


def time_taken(fun):
  # print ('Running '+name)
  print(th.active_count())
  print(th.current_thread())
  def wrapper(n):
    start = time.time()
    fun(n)
    end = time.time()
    # print('Time taken by '+name,end-start)
  return wrapper

# def threading_info(func):
#   # def wrapper(w):
#   # return wrapper
#     return lambda x: print('Heya',x)
#   #   return func

@time_taken
def threading_pace(n):
  print('Running a thread')
  t1 = Thread(target=task,args=(n,))
  t2 = Thread(target=task,args=(n,))
  t1.start()
  t2.start()
  t1.join()
  t2.join()

if __name__ == '__main__':
  num = 5000000
  threading_pace(num)
  print('MAIN')
  # print(threading_info())