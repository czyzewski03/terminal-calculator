#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print('Usage: [command] [operand] ...')
    sys.exit()
function = sys.argv[1]
operands = sys.argv[2:]

print(function)
print(operands)