#!/usr/bin/env python

import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format= '%(asctime)s - %(levelname)s - %(message)s')

def sum_(operands):
    """Adds all arguments in the order they are provided."""
    answer = operands[0]
    for arg in operands[1:]:
        logging.debug(f'arg: {arg}')
        answer += arg
        logging.debug(f'answer: {answer}\n')
    return answer

def difference(operands):
    """Subtracts all arguments from each other in the order they are provided."""
    answer = operands[0]
    for arg in operands[1:]:
        answer -= arg
    return answer

def product(operands):
    """Multiplies all arguments in the order they are provided."""
    answer = operands[0]
    for arg in operands[1:]:
        answer *= arg
    return answer
    
def quotient(operands):
    answer = operands[0]
    try:
        for arg in operands[1:]:
            answer /= arg
        return answer
    except ZeroDivisionError:
        print('ERROR: Cannot divide by zero')
        sys.exit()


if len(sys.argv) < 2:
    print('Usage: [command] [operand] ...')
    sys.exit()
function = sys.argv[1]
operands = [float(x) for x in sys.argv[2:]]

addition_commands = ['sum', 'add', 'addition']
subtraction_commands = ['difference', 'subtract', 'subtraction']
multiplication_commands = ['product', 'multiply', 'multiplication']
division_commands = ['quotient', 'divide', 'division']

if function in addition_commands:
    answer = sum_(operands)
elif function in subtraction_commands:
    answer = difference(operands)
elif function in multiplication_commands:
    answer = product(operands)
elif function in division_commands:
    answer = quotient(operands)

if answer == int(answer):
    print(int(answer))
else:
    print(answer)