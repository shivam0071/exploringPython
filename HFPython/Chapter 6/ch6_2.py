james = {}
julie = {}
mikey = {}
sarah = {}


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (min,sec)=time_string.split(splitter)
    return (min+'.'+sec)

#Thats how i made
# def openItUp(file_name,ath_data):
#     try:
#         with open(file_name) as yo:
#             data = yo.readline()
#             data = data.strip().split(',')
#
#             ath_data['Name'] = data.pop(0)
#             ath_data['DOB'] = data.pop(0)
#             ath_data['Times'] = ath_data['Times'] = data
#             print(ath_data['Name'] + "'s fastest times are: " +
#                   str(sorted(set([sanitize(t) for t in ath_data['Times']]))[0:3]))
#             return ath_data
#
#     except IOError as err:
#         print(err)
#         return None

#
# sarah = openItUp('sarah2.txt',sarah)
# james = openItUp('james2.txt',james)
# julie = openItUp('julie2.txt',julie)
# mikey = openItUp('mikey2.txt',mikey)


#thats how they made


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
            return({'Name' : templ.pop(0),
            'DOB' : templ.pop(0),
            'Times': str(sorted(set([sanitize(t) for t in templ]))[0:3])})
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

james = get_coach_data('james2.txt')
print(james['Name'] + "'s fastest times are: " + james['Times'])