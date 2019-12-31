import random
import json
import string



def random_list_generator(a, b):
    return [ random.randint(a, b) for _ in range(500)]

random_list_gen = lambda a, b :[random.randint(a, b) for _ in range(10)]

# list1 = random_list_gen(100, 500)
# list2 = random_list_gen(501, 1000)

list1 = [2,3,4,5,6,7]
list2 = [[10,11],10,13,14]
print(list1)
print(list2)

print(len(set(list1)))

dic = dict(zip(list1, list2))
print(dic)
dictionaryToJson = json.dumps(dic, indent=2)
print(dictionaryToJson)

list3 = json.dumps(list1)
print(list3, type(list3))
list4 = json.loads(list3)
print(list4, type(list4))

#with open('demo1.json', 'w') as o:
#    o.write(dictionaryToJson)


