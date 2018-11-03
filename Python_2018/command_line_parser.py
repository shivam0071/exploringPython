# https://docs.python.org/2/howto/argparse.html#id1
# import argparse
# parser = argparse.ArgumentParser()
# parser.parse_args()

#RUN
# python command_line_parser.py --h
# usage: command_line_parser.py [-h]
#
# optional arguments:
#   -h, --help  show this help message and exit
#
# C:\Users\Admins\PYTHON\exploringPython\Python_2018>


#POSITIONAL ARGUMENTS

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print (args.echo)

# python command_line_parser.py --h
# usage: command_line_parser.py [-h] echo
#
# positional arguments:
#   echo
#
# optional arguments:
#   -h, --help  show this help message and exit


# python command_line_parser.py echo
# echo


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print (args.echo)

# python prog.py -h
# usage: prog.py [-h] echo
#
# positional arguments:
#   echo        echo the string you use here
#
# optional arguments:
#   -h, --help  show this help message and exit



# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number")
# args = parser.parse_args()
# print (args.square**2)

# $ python prog.py 4
# Traceback (most recent call last):
#   File "prog.py", line 5, in <module>
#     print args.square**2
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number",
#                     type=int)
# args = parser.parse_args()
# print (args.square**2)

#WORKS


#OPTIONAL ARGUMENTS

# It needs some value
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print ("verbosity turned on")

# $ python prog.py --verbosity 1
# verbosity turned on
# $ python prog.py
# $ python prog.py --help
# usage: prog.py [-h] [--verbosity VERBOSITY]
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --verbosity VERBOSITY
#                         increase output verbosity
# $ python prog.py --verbosity
# usage: prog.py [-h] [--verbosity VERBOSITY]
# prog.py: error: argument --verbosity: expected one argument


# -v as a flag
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#    print "verbosity turned on"

#SHORT OPTIONS
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     action="store_true")
# parser.add_argument("echo")
# args = parser.parse_args()
# if args.verbose:
#     print ("verbosity turned on")
# print (args.echo)
# $ python prog.py -v
# verbosity turned on
# $ python prog.py --help
# usage: prog.py [-h] [-v]
#
# optional arguments:
#   -h, --help     show this help message and exit
#   -v, --verbose  increase output verbosity



#COMBINING THEM
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print ("the square of {} equals {}".format(args.square, answer))
# else:
#     print (answer)

# The Order doesn't matter


# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print ("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print ("{}^2 == {}".format(args.square, answer))
# else:
#     print (answer)

# python prog.py 4 -v 3
# this is bug as no verbose is shown for value 3 lets fix this by restricting the values the --verbosity option can accept


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print ("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print ("{}^2 == {}".format(args.square, answer))
else:
    print (answer)


# Add required=True in optional arguments to make them required