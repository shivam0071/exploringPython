# https://www.spoj.com/problems/PRIME1/

def prime2(start, end):
  res = []
  a = [False] * 2 + [True] * (end - 1)
  # print(a, len(a))
  for (n, isprime) in enumerate(a):
    if isprime:
      if not n < start:
          # yield  n
        res.append(n)
      for i in range(n*n, end+1 , n):
        a[i] = False
  return res
#
#
# tescase = int(input())
# while tescase > 0:
#   start,end = map(int,input().split(' '))
#   for item in prime2(start, end):
#     print(item)
#   tescase -= 1

import math

def prime_sieve(n):
    """Use the Sieve of Eratosthenes to list primes 0 to n."""
    primes = list(range(n+1))
    primes[1] = 0
    for i in range(4, n+1, 2):
        primes[i] = 0
    for x in range(3, int(math.sqrt(n))+1, 2):
        if primes[x]:
            for i in range(2*primes[x], n+1, primes[x]):
                primes[i] = 0
    return filter(None, primes)

def ranged_primes(x, y):
    """List primes between x and y."""
    # primes = prime_sieve(int(math.sqrt(y)))
    # print(list(primes))
    primes = prime2(x,int(math.sqrt(y)))
    print(primes)
    return [n for n in range(x, y) if all(n % p for p in primes)]

print(ranged_primes(0, 100))