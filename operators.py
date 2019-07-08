#!/usr/bin/env python

import sys

def sum_(operands):
    """Adds all arguments in the order they are provided."""
    answer = operands[0]
    for operand in operands[1:]:
        answer += operand
    return answer

def difference(operands):
    """Subtracts all arguments from each other in the order they are provided."""
    answer = operands[0]
    for operand in operands[1:]:
        answer -= operand
    return answer

def product(operands):
    """Multiplies all arguments in the order they are provided."""
    answer = operands[0]
    for operand in operands[1:]:
        answer *= operand
    return answer
    
def quotient(operands):
    answer = operands[0]
    try:
        for operand in operands[1:]:
            answer /= operand
        return answer
    except ZeroDivisionError:
        print('ERROR: Cannot divide by zero')
        sys.exit()