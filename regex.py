#! /usr/bin/env python3
""" Program that takes an infix Regular Expression and a text file, and checks if each line of that file matches the given RE. """

# argparse for cmd taking in line arguments
import argparse
# algorithm implementations
import ShuntingYard_RE
import ThompsonConstruct

#
#create argparser object
#description is shown if user adds the universal -h arg for help
#parser = argparse.ArgumentParser(description='Check if each line of the given file is a match for the given infix Regular Expression\nE.G. regex.py (a.b|b*) myfile.txt')

# Get infix Regular Expression
infix = "(a.b|b*)"
# Convert to postfix
postfix = ShuntingYard_RE.toPostfix(infix)
# Create NFA from postfix expression
nfa = ThompsonConstruct.toNFA(postfix)

print(f"Infix: {infix}")
print(f"Postfix: {postfix}")
print(f"thompson: {nfa}")

# Open file in read mode
# "with" lets you get a value from something that would normally require try/catch statements https://www.python.org/dev/peps/pep-0343/
with open("file.txt", "r") as file:
    for line in file:
        # Remove newline character from end of line
        # rstrip removes the given character/s from the end of a string https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip
        line = line.rstrip('\n')
        
        # Pass line of text into our NFA as string, report match?
        match = nfa.match(line)
        print(f"Match '{line}': {match}")