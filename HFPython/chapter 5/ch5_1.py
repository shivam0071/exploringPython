james = []
try:
    with open('james.txt') as jamy:
       data = jamy.readline()
       #james = data  #makes a string
       james = data.strip().split(',')  #makes a list ...as it cuts at comma and assign to the list  #method chaining
    with open('julie.txt') as juf:
        data = juf.readline()
    julie = data.strip().split(',')
    with open('mikey.txt') as mif:
        data = mif.readline()
    mikey = data.strip().split(',')
    with open('sarah.txt') as saf:
        data = saf.readline()
    sarah = data.strip().split(',')
except IOError as err:
    print(err)

# print(james)
# #print(type(james))
# print(julie)
# print(mikey)
# print(sarah)

print(sorted(james))
# print(sorted(julie))
# print(sorted(mikey))
# print(sorted(sarah))


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (min,sec)=time_string.split(splitter)
    return (min+'.'+sec)

# for i in range(len(james)):
#     james[i]=Sanitize(james[i])

# clean_james = []
# clean_julie = []
# clean_mikey = []
# clean_sarah = []

# for each_t in sarah:
#     clean_mikey.append(sanitize(each_t))
# for each_t in mikey:
#     clean_julie.append(sanitize(each_t))
# for each_t in julie:
#     clean_james.append(sanitize(each_t))
# for each_t in james:
#     clean_sarah.append(sanitize(each_t))

# clean_james = [sanitize(m) for m in james]  #Comprehending lists - creating a new list from an existing list
# clean_julie = [sanitize(m) for m in julie]
# clean_mikey = [sanitize(m) for m in mikey]
# clean_sarah = [sanitize(m) for m in sarah]



# print(sorted([sanitize(m) for m in james]))
# print(sorted([sanitize(m) for m in julie]))
# print(sorted([sanitize(m) for m in mikey]))
# print(sorted([sanitize(m) for m in sarah]))
#
# james = sorted([sanitize(m) for m in james])  #Comprehending lists - creating a new list from an existing list
# julie = sorted([sanitize(m) for m in julie])
# mikey = sorted([sanitize(m) for m in mikey])
# sarah = sorted([sanitize(m) for m in sarah])
#
#
# unique_james = []
# unique_julie = []
# unique_mikey = []
# unique_sarah = []
#
# for i in james:
#    if i not in unique_james:
#        unique_james.append(i)
#
# for i in julie:
#    if i not in unique_julie:
#        unique_julie.append(i)
#
# for i in mikey:
#    if i not in unique_mikey:
#        unique_mikey.append(i)
#
# for i in sarah:
#    if i not in unique_sarah:
#        unique_sarah.append(i)
#
#
# print(unique_james[0:3])
# print(unique_julie[0:3])
# print(unique_mikey[0:3])
# print(unique_sarah[0:3])

print(sorted(set(sanitize(m) for m in james))[0:3])
print(sorted(set(sanitize(m) for m in sarah))[0:3])
print(sorted(set(sanitize(m) for m in mikey))[0:3])
print(sorted(set(sanitize(m) for m in julie))[0:3])
