import pickle
from nester import nester_ch2

man = []
other_man = []
#
# try:
#     data = open('sketch.txt')
#     for each_line in data:  #to be more specific than generic and avoiding silent exceptions that may occur
#         try:
#             (role,line_spoken) = each_line.split(':',1)
#             line_spoken = line_spoken.strip()
#             if role == 'Man':
#                 man.append(line_spoken)
#             elif role == 'Other Man':
#                 other_man.append(line_spoken)
# #         except ValueError:
# #             pass  #null statement
# #
# #     data.close()
#
# except IOError:
#     print('The File is missing')
#
# try:
#     with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_files:  #The “b” tells Python to open your data files in BINARY
#         pickle.dump(man, man_file)
#         pickle.dump(other_man, other_files)
# except IOError as err:
#     print('File error: ' + str(err))
# except pickle.PickleError as perr:
#     print('Pickling error: ' + str(perr))

new_man = []
try:
    with open('man_data.txt','rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
        print('File errorss: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

nester_ch2.print_lol(new_man,True,1)