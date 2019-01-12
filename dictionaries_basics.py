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