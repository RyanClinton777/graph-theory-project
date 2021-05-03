# Graph Theory Project - REGEX Search
## Description
This is my submission for the **Graph Theory** Module in Semester 2 of year 3 in **Computing in Software Development BSc**.

It is a console-based program written in Python 3, which allows the user to search for certain patterns/character sequences in a text file, using **Regular Expressions (REGEX)**.

The user inputs a text file (path), and a REGEX search pattern, and the program will print lines from the file where the matches are found.

Indidentally, This was done in Ubuntu Linux through WSL.

## Instructions
Requires some version of Python. Only tested with Python3.

The main file is regex.py.
The program has two positional arguments:
* **infix** - a regular expression in infix notation
* **filepath** - a filepath or filename (if in the same directory) for a text file
````
>python3 regex.py [infix] [filepath]

E.G:
>python3 regex.py "(a.b|b*)" "file.txt"
OR
>python3 regex.py "(a.b|b*)" "/home/user/repo/graph-theory-project/file.txt"

````
![image](https://user-images.githubusercontent.com/58789023/116160818-9d818000-a6ea-11eb-99ea-ae344fca4926.png)

![image](https://user-images.githubusercontent.com/58789023/116934327-c1017900-ac5c-11eb-96a7-ab98b23cd167.png)


The user alternatively run a set of tests (from the regTests.py file) with the optional arg ````--test````
````
>python3 regex.py "" "" --test
````
![image](https://user-images.githubusercontent.com/58789023/116934427-e2626500-ac5c-11eb-8a32-a8b54d9e3fa1.png)


## Algorithm
This program works by applying two algorithms to the given regular expression (RE): 
1. The **Shunting Yard** algorithm - to convert the given infix RE to postfix notation
2. **Thompson Construction** algorithm - to convert that postfix RE into an **NDA (Non-deterministic Finite Automaton).**

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

### Thompson Construction - Convert a postfix RE to an NFA (Non-deterministic Finite Automaton)
This algorithm allows us to convert a postfix Regular Expression, into an **NFA (Non-deterministic Finite Automaton)**.

In "NFA" - "Non-deterministic" means it allows many next states and empty(ε, e for simplicity) transitions; and "Finite" means it has a finite number of states ([As explained here](https://www.javatpoint.com/non-deterministic-finite-automata)). What this allows us to do, is essentially be in multiple states at once in one of these automata. 

These e transitions are essential for this algorithm, as they allow us to create a single start and end state to every NFA, which act as standardised interfaces to plug them in to eachother. We can use these mechanics to attatch nfas for each set of operands and operators until we have an NFA that incorperates the entire RE.

#### Operators
(new state arrows are empty unless specified)
##### Concatination (*)
Take a.b
'a' and 'b' as NFAs look like this:

![image](https://user-images.githubusercontent.com/58789023/116156273-28f71300-a6e3-11eb-8cea-8f119543241f.png)

So to create an NFA for a.b (a concatinate/followed by b), we just need to run our string through them consecutively, only accepting if it makes it through both:
1. Make the end point of a no longer an accept state
2. Make the end point of a point to the start state of b

![image](https://user-images.githubusercontent.com/58789023/116157034-33fe7300-a6e4-11eb-97a5-b9c5ce87a8a8.png)

##### Kleen Star (\*)
Kleen star means 0 or more
For example: a* would accept "", "a", "aa" etc
1. Create new start and end states
2. Make the new start state point to the old start state, and the new end state
3. Make the old end state no longer accept, and now point to both the new end state, and old start state

![image](https://user-images.githubusercontent.com/58789023/116158437-96587300-a6e6-11eb-8b28-916e7b8f9a34.png)

##### OR (|)
Or. Either.
E.g. a|b:

1. Create new end state
2. Create new start state with arrows to the start state of both operand NFAs (a and b)
3. Make end states of both NFAs no longer accept
4. Make end states of both NFAs point to the new end state

![image](https://user-images.githubusercontent.com/58789023/116159121-99a02e80-a6e7-11eb-9e30-afa5d218f3ee.png)

#### Matching
To check if a string matches this DFA:
````
Create stack of current and previous states
occupy and explore this state (including from consecutive empty arrows)
For each character (c) in string:
  previous states = current states
  current states = []
  for state in previousStates:
    If current state has a label matching the current character:
      occupy and explore this state (including from consecutive empty arrows)
      
If any states are accept states:
  return true
else return false
````

## Questions
### What is a regular expression?
**Regular expressions (Regex)** are strings that define a pattern. They are a way of performing advanced, dynamic, programatic find and replace operations on a piece of text. They work by providing a syntax for the user to enter a pattern, which are then checked against the text. *Regular Expressions are equivalent to **Finite Automata*** (although some libraries and implementations can differ from this), and we can think of a regular expression being input by the user as creating an equivalent finite automoton, which then runs on the text.

E.g. "a.b" (a followed/concatinated by b) is equivalent to the following NFA:
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
"A formal language consists of words whose letters are taken from an alphabet and are well-formed according to a specific set of rules." [From Wikipedia](https://en.wikipedia.org/wiki/Formal_language). These can be converted to automata and so can be encoded as regular expressions.
