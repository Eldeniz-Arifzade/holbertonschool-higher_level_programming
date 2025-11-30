#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 65 <= ord(char) <= 90:
            print('{}'.format(char), end='' if char != str[-1] else '\n')
        elif 97 <= ord(char) <= 122:
            print('{}'.format(chr(ord(char) - 32)), end='' if char != str[-1] else '\n')
