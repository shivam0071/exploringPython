#1.) Finding the Largest or Smallest N Items
# You want to make a list of the largest or smallest N items in a collection

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

# OR i would have done using

print(sorted(nums)[-1:-4:-1])
print(sorted(nums,reverse=True)[:3])
print(sorted(nums)[:3])


# how about this?

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(portfolio)

# Pretty Easy Using Heap
print(heapq.nsmallest(3,portfolio,key=lambda x:x['price']))
print(heapq.nlargest(3,portfolio,key=lambda x:x['price']))

#

print(sorted(portfolio,key=lambda x:x['price'])[:3])
print(sorted(portfolio,key=lambda x:x['price'],reverse=True)[:3])

# if N is about the
# same size as the collection itself, it is usually faster to sort it first and take a slice (i.e.,
# use sorted(items)[:N] or sorted(items)[-N:]).


