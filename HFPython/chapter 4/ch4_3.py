
# try:
#     data = open('missing.txt')
#     print(data.readline(), end='')
# except IOError as err:
#     print('File error' +str(err))
# finally:
#     if 'data' in locals():  #The locals() BIF returns a collection of names defined in the current scope.
#         data.close()
#



#we can use the same thing as

try:

    with open('any_text.txt','w') as data2:
        print("Its my life",file = data2)

except IOError as err:

    print("File Error "+str(err))

# with open('man_data.txt', 'w') as man_file, open('other_data.txt’, 'w’) as other_file:
# print(man, file=man_file)
# print(other, file=other_file)