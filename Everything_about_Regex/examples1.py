# 11/12/2018
# 8.09 PM


# 1.) Regex to find the double word in a para
# egrep -i '\<([a-z]+) +\1\>' files



import re

para = '''Whoever popularized the use of "lo-fi" cannot be determined definitively.[7] 
It is generally suggested that The the term was popularized through William Berger's weekly half-hour 
radio show on the New Jersey-based independent radio station WFMU, titled "Low-Fi", which ran 
from 1986 to 1987.[7][8] The the program contents consisted entirely of contributions solicited via 
mail[9] and lasted from 6 to 6:30pm on Fridays, which was a prime time slot.[8] In the the Fall 1986 
issue of the WFMU magazine LCD, the program was described as "home recordings produced on 
inexpensive equipment. Technical primitivism coupled with brilliance."[8] By the end of the 
decade, qualities such such as "home-recorded," "technically primitive," and and and"inexpensive equipment" 
were commonly associated with the "lo-fi" label.[10]'''

# 1.) Regex to find the double word in a para using python

co = re.compile(r"\b([A-Za-z]+)\b +\1\b")

print(co.findall(para))
print([x for x in co.finditer(para)])
# print(para[58:6])

co2 = re.compile(r"\b([A-Za-z]+)\b +\1\b(?: +\1\b)?",re.IGNORECASE)
print(co2.findall(para))
print([x for x in co2.finditer(para)])

