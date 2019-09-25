#!/usr/bin/env python

import sys
import shelve

import operators as op

def to_float(number):
    """Converts numbers and variables to floats."""
    if number.isalpha():
        try:
            return float(symbols[number])
        except KeyError:
            print(f"'ERROR: Variable '{number}' does not exist")
            sys.exit()
    else:
        return float(number)


symbols = shelve.open('symbols')
symbols['PI'] = 3.141592653589793
symbols['E'] = 2.718281828459045

# Checks that the function and operand variables have been provided.
if len(sys.argv) < 2:
    print('Usage: [command] [operand] ...')
    sys.exit()
function = sys.argv[1]
# Converts provided arguments into floats.
operands = [to_float(arg) for arg in sys.argv[2:]]

# Establishes valid keywords for performing an operation.
addition_commands = ['sum', 'add', 'addition', 'plus', '+']
subtraction_commands = ['difference', 'subtract', 'subtraction', 'minus', '-']
multiplication_commands = ['product', 'multiply', 'multiplication', '*']
division_commands = ['quotient', 'divide', 'division', '/']

# Calculates the answer using the correct function.
if function in addition_commands:
    answer = op.sum_(operands)
elif function in subtraction_commands:
    answer = op.difference(operands)
elif function in multiplication_commands:
    answer = op.product(operands)
elif function in division_commands:
    answer = op.quotient(operands)

# Assigns value to a given variable.
elif function == 'assign':
    variable = sys.argv[2].lower()
    value = to_float(sys.argv[3])
    if variable.isalpha() and len(variable) == 1:
        symbols[variable.lower()] = value
        print(f"'{variable}' is set to {value}")
    else:
        print(f"ERROR: '{variable}' is not a valid variable name")
        print('Values can only be assigned to single letters')
    symbols.close()
    sys.exit()

else:
    print(f"ERROR: Command '{function}' not recognised")
    sys.exit()

# Converts answer to integer, if applicable.
if answer.is_integer():
    answer = int(answer)
print(answer)

symbols['ans'] = answer
symbols.close()