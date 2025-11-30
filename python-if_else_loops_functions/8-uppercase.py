#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            print('{}'.format(chr(ord(char) - 32)), end='' if char != str[-1] else '\n')
        else:
            print('{}'.format(char), end='' if char != str[-1] else '\n')
