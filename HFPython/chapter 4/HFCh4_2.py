from nester import nester_ch2
man = []
other_man = []

try:
    data = open('sketch.txt')
    for each_line in data:  #to be more specific than generic and avoiding silent exceptions that may occur
        try:
            (role,line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other_man.append(line_spoken)
        except ValueError:
            pass  #null statement

    data.close()

except IOError:
    print('The File is missing')

# try:
#     man_file = open('man_data.txt','w')
#     other_man_file = open ('other_data.txt','w')
#     print(man,file= man_file)
#     print(other_man,file=other_man_file)
# except IOError:
#     print('The Files are Missing')
# finally:
#     man_file.close()
#     other_man_file.close()

try:
    with open('man_data.txt',"w") as man_file,open('otherman_data.txt',"w") as other_man_file:
       nester_ch2.print_lol(man,True,0,man_file)
       nester_ch2.print_lol(other_man,True,0,other_man_file)

except IOError as err:
    print("File Error "+str(err))



# with open("man_data.txt") as man_file,open("otherman_data.txt") as other_man_file:
#     print(man_file.readline())
#     print(other_man_file.readline())