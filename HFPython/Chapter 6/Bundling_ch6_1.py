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

sarah = openItUp('sarah2.txt')

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (min,sec)=time_string.split(splitter)
    return (min+'.'+sec)

# (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
# print(sarah_name + "'s fastest times are: " +str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data['Name'] + "'s fastest times are: " +
str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))