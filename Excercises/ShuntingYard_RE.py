#! /usr/bin/env python3
""" Shunting Yard Implementation Test"""
# Note: I think "functions" in the psudocode on wikipedia refers to things like ^. Maybe implement this later

# Convert an infix regular expression (string) to a postfix one.
def toPostfix(infix):
    """ Perform shunting yard algorithm on a intfix regular expression, converting it to postfix"""
    output = ""  # Output stack - the numbers in our expression
    operators = "" # Operator/special character stack (using string for ease but could be a list)
    precedence = {"*": 100, ".": 90, "|": 80} # Operator precedence dictionary - operator characters mapped to an arbitrary numeric value representing their precedence
    
    #Loop through characters
    for c in infix:
        # If c is a special character
        if c in {"*", ".", "|"}:
            # While there is still an operator left at the top of the stack
            #       AND the operator at the top of the stack has greater precedence
            #       OR the operator at the top of the stack has equal precedence and the token is left associative (don't know what this means, ignoring for now)
            #       AND that operator is not a left parenthesis '('
            # Note: \ tells python that a statement will continue on to the next line
            while len(operators) > 0 and operators[-1] != '(' and precedence[operators[-1]] >= precedence[c]:
                # Pop the operator from the operator stack onto the output queue.
                output += operators[-1]
                operators = operators[:-1]
            # Push it onto the operator stack
            operators += c
        # Else if token is a left parenthesis (
        elif c == "(":
            # Push c to operator stack
            operators += c
        elif c == ")":
            while operators[-1] != "(":
                # Pop the operator from the operator stack onto the output queue.
                output += operators[-1]
                operators = operators[:-1]
            # If there is a left bracket at the top of the stack, remove it
            if operators[-1] == '(':
                # Pop the operator from the operator stack and discard it
                operators = operators[:-1]
            # if there is a function token at the top of the operator stack... (Ignoring this for now)
        #Else if c is non-special
        else:
            output += c

    # If there are any operators left in the stack, append to output
    while len(operators) > 0:
        # Push operator from top of stack to output
        output += operators[-1]
        # Remove top operator from stack
        operators = operators[:-1]
    return output

#This if statement allows us to only run the following code if this file is run directly as a script. Common in Python, good for tests.
if __name__ == "__main__":
    infix = "a.(b.b)*.a" # Works for any alphabet

    # f strings allow us to insert expressions inside curly brackets, just a convenient way of formatting prints.
    print(f"Infix:   {infix}")
    print(f"Postfix: {toPostfix(infix)}")