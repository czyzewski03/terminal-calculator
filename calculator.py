#!/usr/bin/env python

import sys
import shelve

import operators as op

def to_float(number):
    """Converts numbers and variables to floats."""
    if number.isdigit():
        return float(number)
    elif number.isalpha():
        try:
            return float(shelf_file[number])
        except KeyError:
            print(f"'ERROR: Variable '{number}' does not exist")
            sys.exit()


shelf_file = shelve.open('variables')

# Checks that the function and operand variables have been provided.
if len(sys.argv) < 2:
    print('Usage: [command] [operand] ...')
    sys.exit()
function = sys.argv[1]

# Assigns value to a given variable.
if function == 'assign':
    variable = sys.argv[2].lower()
    value = to_float(sys.argv[3])
    if variable.isalpha() and len(variable) == 1:
        shelf_file[variable] = value
        print(f"'{variable}' is set to {value}")
    else:
        print(f"ERROR: '{variable}' is not a valid variable name")
        print('Values can only be assigned to single letters')
    shelf_file.close()
    sys.exit()

# Converts provided arguments into floats.
operands = []
for argument in sys.argv[2:]:
    operands.append(to_float(argument))

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

# Converts answer to integer, if applicable.
if answer == int(answer):
    answer = int(answer)
print(answer)

shelf_file['ans'] = answer
shelf_file.close()