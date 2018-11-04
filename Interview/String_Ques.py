
# 1.) Ques - You need to split a string into fields, but the delimiters
# (and spacing around them) aren’t
# consistent throughout the string.

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print (re.split(r'[;,\s]\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']