#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>\n')
    elif argv[2] == '+':
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], add(int(argv[1]), int(argv[3]))))
    elif argv[2] == '-':
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], sub(int(argv[1]), int(argv[3]))))
    elif argv[2] == '*':
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], mul(int(argv[1]), int(argv[3]))))
    elif argv[2] == '/':
        print('{} {} {} = {}'.format(argv[1], argv[2], argv[3], div(int(argv[1]), int(argv[3]))))
    else:
        print('Unknown operator. Available operators: +, -, * and /\n')
    sys.exit(1)