# 11/12/2018
# 8.09 PM


# 1.) Regex to find the double word in a para
# egrep -i '\<([a-z]+) +\1\>' files

# Python Specific

# 1.) use \b in place of them for exact match **
# 2.) use ?: inside a parenthesis to use it as a subexpression and not as a group


import re

para = '''Whoever popularized the use of "lo-fi" cannot be determined definitively.[7] 
It is generally suggested that The the term was popularized through William Berger's weekly half-hour 
radio show on the New Jersey-based independent radio station WFMU, titled "Low-Fi", which ran 
from 1986 to 1987.[7][8] The the program contents consisted entirely of contributions solicited via 
mail[9] and lasted from 6 6 to 6:30pm on Fridays, which was a prime time slot.[8] In the the Fall 1986 
issue of the WFMU magazine LCD LCD the program was LCD described as "home recordings produced on 
inexpensive equipment. Technical primitivism coupled with brilliance."[8] By the end of the 
decade, qualities such such as "home-recorded," "technically primitive," and and and"inexpensive equipment" 
were commonly associated with the "lo-fi" label.[10]'''

# 1.) Regex to find the double word in a para using python

co = re.compile(r"\b([A-Za-z]+)\b +\1\b")

print(co.findall(para))
print([x for x in co.finditer(para)])
# print(para[58:6])

# 3 matches with optional
co2 = re.compile(r"\b([A-Za-z]+)\b +\1\b(?: +\1\b)?",re.IGNORECASE)
print(co2.findall(para))
print([x for x in co2.finditer(para)])

# DIGITS
co3 = re.compile(r"\b([0-9]+)\b +\1")
print(co3.findall(para))


#2.) Matching string between parenthesis
str2 = '"Matching this" and not this'
co4 = re.compile(r'"[^^]*"')
print(co4.findall(str2))


# 3.) Finding Time
str3 = "This time is 11:55 am but soon it'll be 4:00 pm"
# (1[012]|[1-9]):[0-5][0-9] (am:pm)"
co5 =  re.compile(r"(?:1[012]|[0-9]):[0-5][0-9] (?:am|pm)")
print(re.findall(co5, str3))

# 3.2 Finding time (224 hours clock)
str4 = "This time is 11:55 but soon it'll be 15:30 and after that it'll be 00:59 and then 23:33 & 06:22" \
       "is this correct time 26:22"
co6 = re.compile(r"(?:0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]")
co7 = re.compile(r"(?:[01]?[0-9]|2[0-3]):[0-5][0-9]")
print(re.findall(co7, str4))



#4 Reading a TAG
str5 = '''
<TAG>
              <h1>Some TEXT<h1>
              <h1>Some TEXT<h1>
              <h1>Some TEXT<h1>
              <h1>Some TEXT<h1>
</TAG>
'''

co8 = re.compile(r'<TAG>[\s\S]*?</TAG>')
print(re.findall(co8, str5)[0])