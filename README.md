# Graph Theory Project - REGEX Search
## Description
This is my submission for the **Graph Theory** Module in Semester 2 of year 3 in **Computing in Software Development BSc**.

It is a console-based program written in Python 3, which allows the user to search for certain patterns/character sequences in a text file, using **Regular Expressions (REGEX)**.

The user inputs a text file (path), and a REGEX search pattern, and the program will print lines from the file where the matches are found.

Indidentally, This was done in Ubuntu Linux through WSL.

## Instructions
...

## Algorithm
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
