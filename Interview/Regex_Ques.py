import re
# The \s metacharacter is used to find a whitespace character.
# d+ means match one or more digits

line = 'asdf fjdk; afed, fjek,asdf, foo'
# eg1 -
print(re.split(r'[;,\s]\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# [;,\s] - this splits the line if a ; , or space is encountered
# \s* - so if the above pattern is matched then if takes in any number of space
# and split the line for example - fjdk; afed here the matched pattern is (;space)


# eg2 -
# >>> text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# >>> import re
# re.match(r'\d+/\d+/\d+', text1)

# datepat = re.compile(r'\d+/\d+/\d+')
# datepat.match(text1)

# datepat.findall(text)
# ['11/27/2012', '3/13/2013']


# >>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# 'Today is 2012-11-27. PyCon starts 2013-3-13.'


#Shortest match

# >>> str_pat = re.compile(r'\"(.*)\"')
# >>> text1 = 'Computer says "no."'
# >>> str_pat.findall(text1)
# ['no.']
# >>> text2 = 'Computer says "no." Phone says "yes."'
# >>> str_pat.findall(text2)
# ['no." Phone says "yes.']

# here * is gred so it matches everything like for text 2
# so we can use something like ? which is not greed

# >>> str_pat = re.compile(r'\"(.*?)\"')
# >>> str_pat.findall(text2)
# ['no.', 'yes.']


# FLAGS

# >>> text = 'UPPER PYTHON, lower python, Mixed Python'
# >>> re.findall('python', text, flags=re.IGNORECASE)
# ['PYTHON', 'python', 'Python']
# >>> re.sub('python', 'snake', text, flags=re.IGNORECASE)
# 'UPPER snake, lower snake, Mixed snake'