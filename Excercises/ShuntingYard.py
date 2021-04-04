#! /usr/bin/env python3
""" Shunting Yard Implementation Test"""

def toPostfix(infix):
    """ Perform shunting yard algorithm on a intfix expression, converting it to postfix"""
    output = ""  # Output stack - the numbers in our expression
    operators = "" # Operator stack (string = array = stack, just easier than array)
    precedence = {} # Operator precedence dictionary - operator character mapped to an arbitrary numeric value representing its precedence (BOMDAS)
    #Loop through characters
    for c in infix:
        #If c is a number
        if (c.isdigit()):
            output += c
            print("Output is now ", output)
        #Else if c is a function - ignoring these for now
        #Else if c is an operator - + - * / might account for x and division ASCII symbol later
        elif c in {"+", "-", "*", "/"}:
            #operators += c
            # While there is still an operator left at the top of the stack
            #       AND the operator at the top of the stack has greater precedence
            #       OR the operator at the top of the stack has equal precedence and the token is left associative (don't know what this means, ignoring for now)
            #       AND that operator is not a left parenthesis '('
            # Note: \ tells python that a statement will continue on to the next line
            while len(operators > 0 and \
                  precedence[operators[-1]] > precedence[c] and \
                  c != '(':
                # Push operator from top of stack to output - They worded this differently? "pop operators from the operator stack onto the output queue."
                # push top operator to output
                output += operators[-1]
                # remove top operator from operator stack
                operators = operators[:-1}]

#            else if the token is an operator then:
#                while ((there is an operator at the top of the operator stack)
#                    and ((the operator at the top of the operator stack has greater precedence)
#                        or (the operator at the top of the operator stack has equal precedence and the token is left associative))
#                    and (the operator at the top of the operator stack is not a left parenthesis)):
#                    pop operators from the operator stack onto the output queue.
#                push it onto the operator stack.
#            else if the token is a left parenthesis (i.e. "("), then:
#                push it onto the operator stack.
#            else if the token is a right parenthesis (i.e. ")"), then:
#                while the operator at the top of the operator stack is not a left parenthesis:
#                    pop the operator from the operator stack onto the output queue.
#                /* If the stack runs out without finding a left parenthesis, then there are mismatched parentheses. */
#                if there is a left parenthesis at the top of the operator stack, then:
#                    pop the operator from the operator stack and discard it
#                if there is a function token at the top of the operator stack, then:
#                    pop the function from the operator stack onto the output queue.
#        /* After while loop, if operator stack not null, pop everything to output queue */
#        if there are no more tokens to read then:
#            while there are still operator tokens on the stack:
#                /* If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses. */
#                pop the operator from the operator stack onto the output queue.
    return output

#infix
infix = "2+3-5*2"

print(toPostfix(infix))