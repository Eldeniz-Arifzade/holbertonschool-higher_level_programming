#!/usr/bin/python3
def uppercase(str):
    for i in len(str):
        if 97 <= ord(str[i]) <= 122:
            print('{}'.format(chr(ord(str[i]) - 32)), end='' if i < len(n)-1 else '\n')
        else:
            print('{}'.format(str[i]), end='' if i < len(n) - 1 else '\n')
