from itertools import islice, tee


# for idx, data in enumerate(tee('abcdef'), 1):
#     print(idx, data)
#     print()
#     for da in zip(*(islice(data, idx, None))):
#         print(da)

f = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))
print(list(f('abcdef')))