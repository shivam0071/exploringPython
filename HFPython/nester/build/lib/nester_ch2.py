'''
A small module to print the list of list of lists
'''
import sys


def print_lol(the_list,indent=False,level = 0,fh=sys.stdout):
    '''
    The function prints each list element and if it encounters another list it calls itself untill it has an basic data type element
    '''
    for item_0 in the_list:
        if isinstance(item_0,list):
            print_lol(item_0,indent,level+1,fh=sys.stdout)

        else:
            if indent:
                for i in range(level):
                    print("\t",end="",file = fh)

            print(item_0)
