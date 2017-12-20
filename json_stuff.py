import json

li = [False] * 100

# jsonData = '{"name": "Frank", "age": 39}'
# jsonToPython = json.loads(jsonData)
# print(jsonToPython)



pythonDictionary =  li #{'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)
print(dictionaryToJson)


#
# with open('json_file.json1','w') as o:
#     o.write(dictionaryToJson)

with open ('json_file.json1','r') as o:
    jsonToPython = json.loads(o.read())


print(jsonToPython)