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


# CODING TIPS SO FAR
#
# 1.) Try to minimise the use of globals
#
# 2.) Manipulating Globals in a function using global keyword is not recommended (pylint fails)
#
# 3.) this - export abc=67 if written in cmd or shell assigns an OS level variable which can be used inside a program
# import os
# os.environ.get('abc')
#
# 4.) Avoid writing repetitive code...use a function instead
#
# 5.) dates
from datetime import datetime,timedelta
import time

#which is string from time #strftime(datetime_date_obj,format)

#there is also string parse time #strptime(strDate,date_format)

# Today = time.strftime('%Y-%m-%d')
#
# Yesterday = datetime.strftime(datetime.now-timedelta(1), '%Y%m%d')
#
# we can also do today - yesterday which gives
# datetime.timedelta() obj which we can just
# str(diff)  or take out total_seconds() days etc
#
# 6) To run cmd commands directly and. store the output in a variable
# import command
#
# out = command.getstatusoutput('grep pattern' + path)
#  out is tuple
# same thing can be done using subprocess
#
# b = subprocess.check_output(['ls'])
# b is a string
#
# 7.) Use difflib module to compare the lists
#
# for line in difflib.unified_diff(prevfile,curr_file, fromfile= 'file1' , tofile = 'file2',lineterm= ' ' ,n=0):
#   for prefix in ('---','+++','@@'):
#     if line.startswith(prefix)
#         break
#     else:
#       result.append(line)
#
# 8.) subprocess.check_output("ls", "-ltr")
# this executes the ls -ltr
#
# Runs command with arguments and return it's output as a byte string
#
# To capture the standard error in the result use
# stderr = subprocess.STDOUT
#
# 9.) Unix : crontab - for job scheduling
#
# use cronta for job scheduling
# -e - edit
# -l - to view
# -r to delete
#
# crontab -e
# min date dom mon dow command
#
# 30 12 * * * echo "Hello World" > /tmp/abc.txt
#
# 10.) To run unix commands on python
# use
# 1.) OS
# 2.) subprocess
#
# import os
# os.system('pwd | grep abcd')
#
# this outputs what ever the ouput is and
# returns 0 on success
# and some other numbers on failure?
#
# 2.) subprocess -
#
# now subprocess has 2 ways
#
#  a.) out = subprocess.check_output(["ls","-ltr"])
# it returns the output in out
#
# it does not support piping so use..
# but we can use PIPE but with a security issues by using shell=True
#
# output = subprocess.check_output("ls | grep GTR" , shell=True)
#
# b.) Popen
#
# a= subprocess.Popen(["ls"], stdout=subprocess.PIPE)
#
# b = subprocess.Popen(["grep","gtr"], stdin= a.stdout, stdout=subprocess.PIPE)
#
# a.stdout.close()
# out = b.communicate()[0]