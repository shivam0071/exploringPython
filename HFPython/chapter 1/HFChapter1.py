# movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
#
# print(movies)
# movies.insert(1,1975)
# movies.insert(3,1979)
# movies.insert(5,1983)
#
# print(movies)
# movies2 = ["The Holy Grail",1975, "The Life of Brian",1979,"The Meaning of Life",1983]
# print(movies2)
#
# for flick in movies2:
#     #print(flick)
#
#
# count = 0
# while count < len(movies2):
#    # print(movies2[count])
#     count = count + 1

movies2 = ["The Holy Grail",1975, "The Life of Brian",1979,['Graham Chapman', ['Michael Palin',
'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]


#instance of BIF
#
# for chicks in movies2:
#     if isinstance(chicks,list):
#         print('true')
#         for chicks2 in chicks:
#             if isinstance(chicks2,list):
#                 for chicks3 in chicks2:
#                     print(chicks3)
#             else:
#                 print(chicks2)
#     else:
#         print(chicks)



#improving the above thing using a function and recursion

def print_lol(the_list,indent = False,level=0):
    for item_0 in the_list:
        if isinstance(item_0,list):
            print_lol(item_0,indent,level+1)

        else:
            if indent:
             for tab in range(level):
                 print("\t",end="")
            print(item_0)


print_lol(movies2,0)

pokemon = ['ash','misty',['pichu','pikachu','raichu'],'brock',['onix','geodude',['star u','star me']]]

print_lol(pokemon,True)
