james = []
julie = []
mikey = []
sarah = []

def openItUp(file_name):
    try:
        with open(file_name) as yo:
            data = yo.readline()
            return data.strip().split(',')
    except IOError as err:
        print(err)
        return None

james = openItUp('james.txt')
julie = openItUp('julie.txt')
mikey = openItUp('mikey.txt')
sarah = openItUp('sarah.txt')

print(james)
print(julie)
print(mikey)
print(sarah)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (min,sec)=time_string.split(splitter)
    return (min+'.'+sec)

print(sorted(set(sanitize(m) for m in james))[0:3])
print(sorted(set(sanitize(m) for m in sarah))[0:3])
print(sorted(set(sanitize(m) for m in mikey))[0:3])
print(sorted(set(sanitize(m) for m in julie))[0:3])