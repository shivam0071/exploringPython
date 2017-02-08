import pprint  #pprint()  #pformat() ...pretty print
import pyperclip
 
#Some things that i am going to forget

#-------------------------------------------------------------------

print('hello')
print('world')
#output
#hello
#world

#print('hello',end=' ')
print('world')
#output = hello world

#---------------------------------------------------------------------------
#to increase readibility

print('Four score and seven ' + \
      'years ago...')


#-----------------------------------------------------------------------------
"""
str.upper()/lower()

isalpha() returns True if the string consists only of letters and is not blank.

isalnum() returns True if the string consists only of letters and numbers
and is not blank.

isdecimal() returns True if the string consists only of numeric characters
and is not blank.

isspace() returns True if the string consists only of spaces, tabs, and newlines
and is not blank.

istitle() returns True if the string consists only of words that begin with
an uppercase letter followed by only lowercase letters.


>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isdecimal()
True
>>> ' '.isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case'.istitle()
False
>>> 'This Is NOT Title Case Either'.istitle()
False

The startswith() and endswith() methods return True if the string value they
are called on begins or ends (respectively) with the string passed to the
method; otherwise, they return False.

isupper()

islower()
"""
#---------------------------------------------------------------------
#Join and split
"""
The join() method is useful when you have a list of strings that need to be
joined together into a single string value.

>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'


The split()
method does the opposite: It’s called on a string value and returns a list of
strings.

>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']

"""


#---------------------------------------------------------------------
#rjust()  #ljust() 
"""
The rjust() and ljust() string methods return a padded version of the
string they are called on, with spaces inserted to justify the text. The first
argument to both methods is an integer length for the justified string.

>>> 'Hello'.rjust(10)
' Hello'
>>> 'Hello'.rjust(20)
' Hello'
>>> 'Hello World'.rjust(20)
' Hello World'
>>> 'Hello'.ljust(10)
'Hello               '

>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'


The center() string method works like ljust() and rjust() but centers
the text rather than justifying it to the left or right. Enter the following
into the interactive shell:
>>> 'Hello'.center(20)
' Hello '
>>> 'Hello'.center(20, '=')
'=======Hello========'

The
strip() string method will return a new string without any whitespace
"""




#-------------------------------------------------------------------
#copy paste()
"""
Copying and Pasting Strings with the pyperclip Module

>>> import pyperclip
>>> pyperclip.copy('Hello world!')
>>> pyperclip.paste()
'Hello world!'

"""

pyperclip.copy('hey')
pyperclip.paste()

#-------------------------------------------------------------------
#a global variable used inside a function ..
# write global xyz in the method ....now python knows its from the global not local


#----------------------------------------------------------------------
#LISTS

print('***************Lists******************')
#LISTS are mutable whereas STRINGS are not
spam=['hi','hello','bye','bello']

print(spam + ['shaan']) #concatination  ['hi', 'hello', 'bye', 'bello', 'shaan']
print(spam) #['hi', 'hello', 'bye', 'bello']


spam= spam+['shaan','awesome']
print(spam) #['hi', 'hello', 'bye', 'bello', 'shaan', 'awesome']


spam.sort()
print(spam) #['awesome', 'bello', 'bye', 'hello', 'hi', 'shaan']

spam=spam+['Zorro','X-mas','dayum']

print(spam)  #['awesome', 'bello', 'bye', 'hello', 'hi', 'shaan', 'Zorro', 'X-mas', 'dayum']

spam.sort()
print(spam)
#['X-mas', 'Zorro', 'awesome', 'bello', 'bye', 'dayum', 'hello', 'hi', 'shaan']
#x z before a?? acc to ASCII

#SO do this
spam.sort(key=str.lower)
print(spam)

#['awesome', 'bello', 'bye', 'dayum', 'hello', 'hi', 'shaan', 'X-mas', 'Zorro']

#Descending order
spam.sort(reverse=True)
print(spam)

#['shaan', 'hi', 'hello', 'dayum', 'bye', 'bello', 'awesome', 'Zorro', 'X-mas']

spam.sort(reverse=True,key=str.lower)
print(spam)
#['Zorro', 'X-mas', 'shaan', 'hi', 'hello', 'dayum', 'bye', 'bello', 'awesome']



del spam[3]
print(spam)

spam.append('ELectrify')
print(spam)


spam.insert(1,'Hotline BLinge')
print(spam)

spam.remove('bello')
print(spam)
#['Zorro', 'Hotline BLinge', 'X-mas', 'shaan', 'hello', 'dayum', 'bye', 'awesome', 'ELectrify']
print(spam.index('shaan'))

spam[1]='open ur eyes'
print(spam)

#['Zorro', 'open ur eyes', 'X-mas', 'shaan', 'hello', 'dayum', 'bye', 'awesome', 'ELectrify']
#replaced

#--------------------------------------------------------------------------
#TUPLES

#tuples are same as lists but are immutable and assigned using paranthesis ()
print()
print('***************Tuples******************')
home=('as','long',)

print(home)

print(type(spam))
print(type(home))
print(type('shaan'))
print(type(('shaan',)))



#---------------------------------------------------------------------------
#Dictionaries

print()
print('***************Dictionaries******************')

targets={'goal':'money','for':'everyone to be happy','how':'work hard and find ways to earn extra money'}
print(targets)


# important methods,....keys(),values(),items()

for j in targets.values():
    print(j)
for j in targets.keys():
    print(j)
for j,k in targets.items():
    print(j+" "+k)

print(targets['goal'])

print('poal' in targets.keys())

# get() method... accesses the value using a key and also takes a default value in case of a key is missing

print(targets.get('how',0))
print(targets.get('life','is getting worse but never give up'))
    
targets.setdefault('life','life is getting worse but never give up')
print(targets)
targets.setdefault('life','life is good')
print(targets  )  #no change


targets['life'] = 'LP is love LP is life'
print(targets) #changes


print('********************** A Small Program*********************')
#counts no of characters
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
#print(count)
pprint.pprint(count)
print(pprint.pformat(count)) #same


print('*********************************************************')
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0

    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
        
    return numBrought
print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))


input()
#-----------------------------------------------------------------------------

