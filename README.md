# Graph Theory Project - REGEX Search
## Description
This is my submission for the **Graph Theory** Module in Semester 2 of year 3 in **Computing in Software Development BSc**.

It is a console-based program written in Python 3, which allows the user to search for certain patterns/character sequences in a text file, using **Regular Expressions (REGEX)**.

The user inputs a text file (path), and a REGEX search pattern, and the program will print lines from the file where the matches are found.

Indidentally, This was done in Ubuntu Linux through WSL.

## Instructions
...

## Algorithm
This program works by applying two algorithms to the given regular expression (RE): 
1. The **Shunting Yard** algorithm - to convert the given infix RE to postfix notation
2. **Thompson Construction** algorithm - to convert that postfix RE into an **NDA (Non-Finite Automata).**

It then simply reads each line of the file, and checks if each line of text matches the pattern defined by the RE.

### Shunting Yard - Convert an infix expression to postfix notation
For human reading, different types of expressions (Mathmatical, Regular) are usually written in [**Infix notation**](https://en.wikipedia.org/wiki/Infix_notation). In this notation, operators are placed between the operands that they apply to, and precedence is indicated with (parenthesis), and overall is decided by an [order of operations](https://en.wikipedia.org/wiki/Order_of_operations) rule such as BOMDAS. E.g. 2+2, a.b
  
This is appropriate for humans because characters and operations that should apply to them are grouped together in an intuitive and easily intelligable manner.

[**Postfix notation**](https://en.wikipedia.org/wiki/Reverse_Polish_notation) (aka: Reverse Polish notation) Arranges the expression with the operands first, followed by their operators.
* **Infix:** 2 + 5 - 3
* **Postfix:** 2 5 + 3 -

The computer reads left to right. So by the time it reads +, the number stack will contain [2,5]. It applies the operator to the top two numbers on the stack (2+5=7) and puts the result in the stack [7]; then by the time it reaches -, the number stack will contain [7,3], and it does the same thing: (7-3=4). This is a simple example, but it is very efficient when dealing with multiplication and division, expressions with parenthesis etc.

This notation is ideal for computers because:
1. Formulas can be expressed without parenthesis
2. It is convenient to evaluate using stacks
3. It avoids the problems of operator precedence

This according to a document from DePaul University, which gives a much more in depth explaination [Link](https://condor.depaul.edu/ggordon/courses/224/212doc/postfix.txt#:~:text=Postfix%20has%20a%20number%20of,Third%2C%20infix%20operators%20have%20precedence.).

The algorithm works as follows (pseudocode):
```
For each character (c) in infix:
  if c is an operator:
    While there is still an operator left on the stack
      AND the operator at the top of the stack has greater precedence
      AND that operator is not a left parenthesis '(':
        pop the operator from the operator stack onto the output stack
    Push c to the operator stack
  else if c is a left parenthesis '(':
    push c to the operator stack
  else if c is a right parenthesis ')':
    while the top of the operator stack is not a left parenthesis '(':
      Pop the operator from the operator stack onto the output stack.
  else (c is an operand):
    push c to the output stack
    
If there is anything left on the operator stack, push it to output.
```
E.G. (Spaces are just for readability)
1. Infix = "2 + 5" [outputStack] [operatorStack]
2. '2' is an operand > push to output stack [2] []
3. '+' is an operator > push to operator stack (none of the while... logic applies) [2] [+]
4. '5' is an operand > push to output stack [2,5] [+]
5. String finished > Push remaining operators to output [2,5,+] []
6. Postfix = "2 5 +"

My code was adapted from the pseudo code on the [wikipedia page](https://en.wikipedia.org/wiki/Shunting-yard_algorithm#The_algorithm_in_detail).

### Thompson Construction - Convert a postfix RE to an NFA (Non-Finite Automata)
...

## Questions
### What is a regular expression?
**Regular expressions (Regex)** are strings that define a pattern. They are a way of performing advanced, dynamic, programatic find and replace operations on a piece of text. They work by providing a syntax for the user to enter a pattern, which are then checked against the text. *Regular Expressions are equivalent to **Finite Automata*** (although some libraries and implementations can differ from this), and we can think of a regular expression being input by the user as creating an equivalent finite automoton, which then runs on the text.

E.g. "a.b" (a followed/concatinated by b) is equivilent to the following NFA:
![image](https://user-images.githubusercontent.com/58789023/113922922-cf847e00-97df-11eb-90bf-ace16f2b16b3.png)

In normal search operations, an exact phrase must be entered for matches to be found, but regular expressions allow us to do much more advanced searches. 
Some examples of patterns we can account for:
* An indefinite or definite number of unknown characters (wildcards)
* Types of characters (e.g. only allow numbers or letters)
* Words of of a certain length, with a minimum and maximum
* Characters in a given set, or a within specific range; which can apply to characters, numbers, or even special characters.

An expression can be made to match practically any pattern. Two common examples of useful applications of Regex would be finding every email address or phone number in a large piece of text. 
Take the following examples of the same phone number for instance:
* 0915555555
* 091-555-5555
* 091 555 5555

Phone numbers may be written with or without dashes/spaces, email addresses may have varying amounts of characters in each segment, different numbers of dots (.co.uk etc); but a pattern that matches every scenario can easily be written in minutes, and can save countless hours of tedious work doing this manually.

Advanced replacement operations can then be done any matching text if desired. We can: 
* Format data (Dates, etc)
* Standardise spellings (colour/color)
* Fix grammer mistakes (ensure Upper case at the start of every line is a simple example) 
* Truncate or round numbers up or down
* Remove illegal characters
...and practically anything else we like.

### How do regular expressions differ across implementations?
The exact syntax for an operation, and features available depends on the **Regular Expression Engine** being used. These are usually associated with a particular programming language, and are like different Regex languages themselves. These different implementations of regular expressions are called **regex flavors.** Different IDEs, code editors, and Database Management Systems will have their own engines, so it is important to know which one you are working with; for example, most web editors and tools will use the ECMA Javascript variety, wheras eclipse uses a java based flavor; python has it's own regex library.

Sometimes, the same program might use several different flavors for different functions. For example, Visual Studio Code uses a module that works with a RUST-based implementation for file searches, but uses Javascript syntax for code searches. 
  [1]: https://github.com/Microsoft/vscode/issues/24626
  [2]: https://github.com/Microsoft/vscode/issues/8635
  [3]: https://stackoverflow.com/questions/42179046/what-flavor-of-regex-does-visual-studio-code-use

Most Regex engines are very similar in principle, and many simple operations can even be interchangeable between them.



### Can all formal languages be encoded as regular expressions?
...
