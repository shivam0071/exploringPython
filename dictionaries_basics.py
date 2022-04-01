dict = {7:'Key',9:'iii',1:'Value',5:'Abcd'}
print(dict)


# print((sorted(dict.keys())
# get value sorted according to the keys
res = map(lambda y: dict.get(y),sorted(dict.keys()))
print(list(res))

print(sorted(dict.items()))
# print(sorted(dict.items(),key = lambda y:))
ls = [[1,3],[33,1],[110,30],[11,366]]
print(ls)
print(sorted(ls,key=lambda x:x[0]))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

from operator import itemgetter, attrgetter
print(sorted(student_tuples, key=itemgetter(2)))

import collections
def sort_this(ls):
    print(ls)
    res = []
    left_idx = 0
    for idx, data in enumerate(ls[:]):
        if data < 0:
            ls.insert(left_idx, ls.pop(idx))
            left_idx += 1
        elif data > 0:
            ls.append(data)
            res.append(data)
    else:
        for d in res:
            ls.remove(d)
    print(ls)

def sort_this_2_pointers(ls):
    print(ls)
    left = 0
    right = len(ls) - 1
    idx = 0
    while left < right:
        data = ls[left]
        if data < 0:
            ls[idx], ls[left] = ls[left], data
            left += 1
        elif data > 0:
            ls[idx], ls[right] = ls[right], data
            right -= 1
        else:
            left += 1
            idx += 1

    print(ls)

# sort_this([10, 4, -1, -4, 0, 6, 0, -8, -9])

sort_this_2_pointers([10, 4, -1, -4, 0, 6, 0, -8, -9])