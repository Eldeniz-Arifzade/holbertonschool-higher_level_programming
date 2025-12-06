#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(roman_string)
    if roman_string is None or type(roman_string) != str:
        return 0
    if len(roman_list) == 1:
        return roman[roman_list[0]]
    for i in range(0, len(roman_list)-1):
        if roman[roman_list[i]] >= roman[roman_list[i+1]]:
            roman_list[i+1] = roman_list[i] + roman_list[i+1]
        else:
            roman_list[i+1] = roman_list[i+1] - roman_list[i]
    return roman_list[-1]
