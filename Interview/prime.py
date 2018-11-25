import math
import time
def prime(n):
  print ('SQRT Version')
  res = []
  for i in range(2,n):
    if i == 2:
      res.append(i)
      continue
    for x in range(2,int(math.sqrt(i)) + 1):
      if i % x == 0:
        break
    else:
      res.append(i)
  return res

def prime2(num):
  print ('Faster Version')
  a = [False] * 2 + [True] * (num-2)
  for (n, isprime) in enumerate(a):
    if isprime:
      yield  n
      for i in range(n*n, num, n):
        a[i] = False

def time_m(func, n):
  start = time.time()
  func(n)
  end = time.time()
  print('Time Taken', end-start )

if __name__ == '__main__':
  n = 100000000  #50.40650272369385
  # ls = prime(n)
  # print(len(ls))
  # print(ls)
  # print ([x for x in range(2, 100) if all(x % y != 0 for y in range(2, int(math.sqrt(x))+ 1))])

  start = time.time()
  print(len(list(prime2(n))))
  end = time.time()
  print('Time Taken', end-start )



  # time_m(prime, n ) # 17 sec