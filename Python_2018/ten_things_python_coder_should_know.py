# 4th March 2018
# 6.16 pm
# Still confused about life :|

# Some important links /
# https://www.python.org/
# https://docs.python.org/3/
# https://docs.python.org/3/library/index.html

#https://danieltakeshi.github.io/2013/07/05/ten-things-python-programmers-should-know/


# 1.) Python Version Numbers
# Python versions are numbered as A.B.C., where the three letters represent (in decreasing order)
#  important changes in the language. So, for instance, going from 2.7.3 to 2.7.4 means that the Python
#  build made some minor bug fixes, while going from 2.xx to 3.xx represents a major change.


# One important thing to note, though, is that Python 3 is intentionally backwards incompatible.
# new version has better Unicode support and few fixes here and there


# now wtf is Unicode??
# Unicode provides a unique number for every character,
# no matter what the platform,
# no matter what the program,
# no matter what the language.

# Fundamentally, computers just deal with numbers. They store letters and other characters by assigning
#  a number for each one. Before Unicode was invented, there were hundreds of different systems,
#  called character encodings, for assigning these numbers. These early character encodings were
#  limited and could not contain enough characters to cover all the world's languages.
#  Even for a single language like English no single encoding was adequate for all the letters,
#  punctuation, and technical symbols in common use.


# The Unicode Standard provides a unique number for every character, no matter what platform,
#  device, application or language. It has been adopted by all modern software providers and now
#  allows data to be transported through many different platforms, devices and applications without
# corruption. Support of Unicode forms the foundation for the representation of languages and symbols
#  in all major operating systems, search engines, browsers, laptops, and smart phones—plus the Internet
#  and World Wide Web (URLs, HTML, XML, CSS, JSON, etc.). Supporting Unicode is the best way to
#  implement ISO/IEC 10646.


# READ MORE :-
# https://docs.python.org/3/howto/unicode.html

# One-character Unicode strings can also be created with the chr() built-in function, which takes integers and returns a Unicode string of length 1 that contains the corresponding
#  code point. The reverse operation is the built-in ord()
#  function that takes a one-character Unicode string and returns the code point value:


# To check python version
import sys
print("My version Number: {}".format(sys.version))