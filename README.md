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
**Regular expressions (Regex)** are a way of performing dynamic, programatic find and replace operations on a piece of text. They work by providing a syntax for the user to program a pattern, which are then checked against the text.

In normal search operations, an exact phrase must be entered for matches to be found, but regular expressions allow us to do much more advanced searches. 
Some examples of patterns we can account for:
- An indefinite or definite number of unknown characters (wildcards)
- Types of characters (e.g. only allow numbers or letters)
- Words of of a certain length, with a minimum and maximum
- Characters in a given set, or a within specific range; which can apply to characters, numbers, or even special characters

An expression can be made to match practically any pattern. Two common examples of useful applications of Regex would be finding every email address or phone number in a large piece of text. Phone numbers may be written with or without dashes, email addresses may have varying amounts of characters in each segment, different numbers of dots (.co.uk etc); but a pattern that matches every scenario can easily be written in minutes, and can save countless hours of tedious work doing this manually.

Advanced replacement operations can then be done any matching text if desired. We can standardise spellings (colour/color), truncate or round numbers, change cases, validate data and practically anything else we like.

### How do regular expressions differ across implementations?
The exact syntax for an operation depends on the **Regular Expression Engine** being used. These are usually associated with a particular programming language, and are like different languages for RE themselves, though they are all very similar in principle, and often simple searches may even be interchangeable between them.

### Can all formal languages be encoded as regular expressions?
...
