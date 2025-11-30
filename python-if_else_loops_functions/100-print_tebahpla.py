#!/usr/bin/python3
for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'[::-1]):
    print('{}'.format(char) if i % 2 == 0 else char.upper(), end='')
