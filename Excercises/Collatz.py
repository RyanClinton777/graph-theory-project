"""Collatz conjecture"""
# NOTE: This """String literal""" is conventionally used in python for auto-generating docs etc. Good to put the title/purpose at start of file like this.

# ---Collatz Conjecture Sequence
# takes an int and repeatedly:
#   divides it by 2 if it's even, or:
#   multiplies it by 3 and adds 1 if odd. 
# Prints sequence. E.g. 8 > 4 > 2 > 1
# Supposedly, every number should eventually end up at 1.
def collatz(n) :
    # Print first number
    print(n, end = '') # end='' for no newline
    
    #Until number is 1
    while (n != 1):
        # EVEN
        if (n%2 == 0):
            n = int(n/2) #int(n) to cast to int - division returns float.
        # ODD
        else:
            n = int((n*3)+1)
        # Print current number in sequence
        print(" >", n ,end = '')
    print() # New line

# ---PROGRAM CODE---
# Print sequence for 1-10
# This is how to do a simple for loop in python. Note that indexing starts at 0.
for i in range(10):
    collatz(i+1)