# Introduction
It's a calculator that can perform calculations. As the name indicates, it is run from the command line.

To use it, run '[function] [operand] [operand] ...'. No limit should be present on the amount of operands that can be used.

# Basic Operations
To perform the fundamental operations of addition, subtraction, multiplication, and division, the user must specify this as their function (i.e. the first argument passed in). For ease of use, multiple keywords have been implemented that perform the same operation; these are the commands that can be used:
## Addition
'sum', 'add', 'addition', 'plus', '+'
## Subtraction
'difference', 'subtract', 'subtraction', 'minus', '-'
## Multiplication
'product', 'multiply', 'multiplication', '\*'
## Division
'quotient', 'divide', 'division', '/'

# Algebra
## Custom Variables
Users can set their own variables to be used in algebraic operations with the *assign* command. Simply pass the arguments 'assign [symbol] [value]' when running the program in order to set the chosen symbol to a value. Note that, for simplicity, only letters in the alphabet can have a value assigned this way. Even though it is possible for the user to input an uppercase letter as the symbol, this will just be converted to lowercase by the program; to actually invoke the variable in a calculation, it must be input as a lowercase letter.

## Constants
This program has the constants *pi* and *e* built in. They can be used in any calculation simply by typing their name in as uppercase. This is to differenciate them from custom variables the user might have set and also to avoid naming conflicts.

## Last Answer
If the user would like to quickly use the result from the previous calculation, they can use the unique variable *ans* (all lowercase), which stands for 'answer'. When any mathematical operation is run (not including invalid calculations which don't produce an answer), *ans* will be updated with the new value. This happens automatically and requires no input from the user. Do not attempt to manually assign a value to this variable, as this is invalid and will result in an error.

This behaviour mimics the ANS buttons found on many physical calculators, and is used in the same way
