#! /usr/bin/env python3
#The above is called a "shabang" - basically is used to make a program directly executable in linux...
#... by running python at the given directory, with this script as an argument.

import argparse

#argparse is a native py library for taking in args in the command line.
#https://docs.python.org/3/library/argparse.html
#Arguements in python don't need to be given in order, you just specify the arg name (keyword arguments)

#create argparser object
#description is shown if user adds the universal -h arg for help
parser = argparse.ArgumentParser(description='Process some integers.')

#add some arguments
#First arg is "name or flags" - tells py if optional arguments are expected
#simple name for just one argument, or -f etc for optionals like --sum in this case
#nargs = number of args. - '+' = a list of any number, at least one
#metavar = name of arg, mostly for help  messages

#take list of integers
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

# --sum arg, to return the sum of the given number, rather than the highest.
#This is an optional parameter. If we run the program as usual and add --sum at the end, it will
    #dest specifies the name of the object to which the results of parse_args() are returned.
    #action='store_const' - the action to be taken  if this arg (--sum) is given. In this case, the sum() method.
    #default - the action to be taken if the argument isn't given.
    #help is just what is displayed for this arg in -h (help)
# So basically this method will return something to the variable "accumulate":
#   sum if the arg is present
#   max if it isn't
# So later when we do args.accumulate(args.integers) - accumulate will either be the max() method, or the sum() method, and the result of that on those ints will be what is returned.
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

#Just puts the args into a variable
args = parser.parse_args()

# Confused about this - research further...
# I don't think this has anything to do with the actual accumulate method, 
# I think we are just using accumulate as a name for our method "variable" which will be given value of sum() or max() depending on --sum presence
print(args.accumulate(args.integers))