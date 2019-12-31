# Basic and Easy Questions
range

# 1) WAP of reverse a str1ing

str1 = 'A string That Need TO Be Reversed'
print(str1[::-1])

# 2) WAP to split the string a store in a list
print(str1.split())

# 3) WAP to split the string to store only even items
print(str1.split()[::2])
# the thing we learn here is no water how many index you want to jump it always starts with index 0
print(str1.split()[1::2])
# Even for a human

# 4.) WAP to lower the string
print(str1.lower())

# 5.) Swap the cases in the string
# eg - EthanS to eTHANs
print(str1.swapcase())
# Impressive

# 6.) WAP to check if a substring is available in the string
print(str1.find('ver'))
# so it indeed search for a substring...cool

# 7.)  WAP to capitalize the string
print(str1.capitalize())

# 8 WAP to add 3 '*' on both side of the string
str1_len = len(str1)
print(str1_len)
print(str1.center(str1_len+6,'*'))
        # OR
print(format(str1, '*^'+str(str1_len+6)))

#9 ) WAP to hide first 12 digits of a 16 digit account no
account_no = '2233773456788899'
print('*'*12+''+account_no[len(account_no)-4:])

# 10 WAP to remove the traling whitespaces...after that remove the leading white spaces and the both

str2 = '      HELLO     WORLD          '
print(str2)
print(str2.lstrip().rstrip())
print(str2.strip())


#  11 WAP to remove all the vowels

vowels = ['a','e','i','o','u']
print(str1)
print (''.join([ch for ch in str1 if ch.lower() not in vowels]).strip())

# WAP to delete a range of strings
n=10
print(str1[n:])
# 1.) Ques - You need to split a str1ng into fields, but the delimiters
# (and spacing around them) aren’t
# consistent throughout the str1ing.


line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print (re.split(r'[;,\s]\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


c = 'shivamuchiha'
v = [1,2,3,4,5,6,7,8,9,0]
b = 'shivam'

print("{} -> {}".format(c, c[:3:-1]))
print("{} -> {}".format(v, v[:3:-1]))
print("{} -> {}".format(b, b[:3:-1]))