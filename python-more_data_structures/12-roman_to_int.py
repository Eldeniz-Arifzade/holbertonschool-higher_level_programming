#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if len(roman_string) is None or type(roman_string) != str:
        return 0
    s = 0
    for i in range(len(roman_list)-1):
        if roman[roman_string[i]] < roman[roman_string[i+1]]:
            s -= roman[roman_string[i]]
        else:
            s += roman[roman_string[i]]
    return s
