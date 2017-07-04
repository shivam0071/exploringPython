

try:
    data = open('sketch.txt')
    # print(data.readline(), end='')
    # data.seek(0)   #back to start

# for each_line in data:
#     print(each_line, end='')

#
# for each_line in data:
#     if each_line.find(':') != -1:
#         (role,line_spoken) = each_line.split(':',1)
#         print(role, end='')
#         print(' said: ', end='')
#         print(line_spoken, end='')


    # for each_line in data:
    #     try:
    #         (role,line_spoken) = each_line.split(':',1)
    #         print(role, end='')
    #         print(' said: ', end='')
    #         print(line_spoken, end='')
    #     except:
    #         pass  #null statement

    for each_line in data:  #to be more specific than generic and avoiding silent exceptions that may occur
        try:
            (role,line_spoken) = each_line.split(':',1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass  #null statement

    data.close()

except IOError:
    print('The File is missing')


