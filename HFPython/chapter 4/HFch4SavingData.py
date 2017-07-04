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

print(man)
print(other_man)