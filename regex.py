#! /usr/bin/env python3
""" Program that takes an infix Regular Expression and a text file, and checks if each line of that file matches the given RE. """
# E.G: python3 regex.py -re "(a.b|b*)" -file "file.txt"

# argparse for cmd taking in line arguments
import argparse
# algorithm implementations
import ShuntingYard_RE
import ThompsonConstruct
# Tests file
import regTests

# ------ PROGRAM CODE ------
# --- ARGS
# Create argparser object
parser = argparse.ArgumentParser(description='Check if each line of the given file is a match for the given infix Regular Expression \nE.G. regex.py (a.b|b*) myfile.txt')
# Positional args:
group = parser.add_mutually_exclusive_group()
# Regular Expression string (args read in as strings by default) - calling it re because it seems more intuitive for user
parser.add_argument("infix", metavar='InfixRE', help='An Infix Regular Expression.')
# File name/path string
parser.add_argument("filepath", metavar='filepath', help='The file name or file path of the text file.')
# Optional args :
# --test flag to run tests - I wanted the user to be able to input this instead of the positional args, like -h, but it doesn't seem easily possible
parser.add_argument('--test', action='store_true', help='Run tests instead of taking in user inputs')

# --- PARSE ARGS
# Parse args, and get them in dictionary view with vars()
argv = vars(parser.parse_args())
# Get infix Regular Expression
infix = argv['infix']
# Get filepath/name
filepath = argv['filepath'] # "/home/user/repo/graph-theory-project/file.txt" || "file.txt"
# isTest
isTest = argv['test']

# --- ALGORITHMS
# Convert to postfix
postfix = ShuntingYard_RE.toPostfix(infix)
# Create NFA from postfix expression
nfa = ThompsonConstruct.toNFA(postfix)

# --- MATCH
if not isTest:
    print(f"Infix Expression: '{infix}'")
    print(f"Postfix Expression: '{postfix}'")

    # Open file in read mode
    # "with" lets you easily get a value from something that would normally require try/catch statements https://www.python.org/dev/peps/pep-0343/
    with open(filepath, "r") as file:
        for line in file:
            # Remove newline character from end of line
            # rstrip removes the given character/s from the end of a string https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip
            line = line.rstrip('\n')
            
            # Pass line of text into our NFA as string, report match?
            match = nfa.match(line)
            print(f"Match '{line}': {match}")
else:
    regTests.runTests()