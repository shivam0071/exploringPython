#1 WAP to get 2 highest no in a list
ls = [33, 44, 55, 11, 99, 22, 1, 34, 56, 78, 98]

print(sorted(ls)[-2:])

#2 WAP to convert list into DICT

print (dict((key, value) for key, value in enumerate(ls)))

# 3 WAP to flatten a list

ls1 = [1, 2, 3, 4 , [5, 6, 7], 8 ,9, 10, [11, 23 , [33,77, [90, 55,12,334]]], 69, 6969]
print(ls1)
ls2 = []

def flatten(ls):
  for item in ls:
    if isinstance(item, list):
      flatten(item)
      continue
    ls2.append(item)
flatten(ls1)
print(ls2)

#4 WAP to merge 2 dict
dic1 = {'Name': 'Shaan', 'Position': 'Senior Singer'}
dic2 = {'Address':'Nowhere Town', 'Pin': '11223344'}
# print(dict(zip(dic1,dic2)))
# print(dic1.update(dic2))
merged = dic1.copy()#.update(dic2)
merged.update(dic2)
print(merged)

#5 print all keys with vowel as a value
dic3 = {1:'a',2:'c',3:'e'}
vowels = ['a','e','i','o','u']
print([key for key, value in dic3.items() if value in vowels])

#6 WAP to empty a dictionary

dic3.clear()
print(dic3)


#7 wap to get common elements in a list/tuple

ls1 = [1,2,4,44,3,2,1]
ls2 = [44,3,111,99,44]
print(set(ls1).intersection(ls2))

# 8  Different Elements
print(set(ls1) ^ set(ls2))

# shift all the zeros in a list to RHS

ls4 = [1,2,0,44,0,66,0,5644,3,0,33,4]
ls5 = [item for item in ls4 if item != 0]
ls5.extend([0] * (len(ls4) - len(ls5)))
print(ls5)


# 9 WAP to get the key of a dict if the value is present in the dictionary if not present then
# print None

print(dic1)
val = 'Shaan'
for key, value in dic1.items():
  if value == val:
    print(key)
    break
else:
  print(None)


# WAP to capitalize the name and surname
name = 'naruto uzumaki'
print(' '.join([na.capitalize()for na in name.split()]))

# WAP to get user from input ...if he typs stop...stop the prgram
# while(True):
#   user = input('Enter Whatever the heck you want....type stop to end this\n')
#   if user == 'stop':
#     break
#   print(user)
#   print(type(user))

# WAP to conver a list into a string [1,2,3,4,5] -- ['1','2','3']

ls6 = [1,2,3,4,5]
print([str(item)for item in ls])