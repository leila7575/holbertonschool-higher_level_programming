#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
    }
    result = roman_values[roman_string[-1]]
    for i in reversed(range(len(roman_string) -1)):
        if roman_values[roman_string[i]] >= roman_values[roman_string[i + 1]]:
            result += roman_values[roman_string[i]]
        else:
            result -= roman_values[roman_string[i]]
    return result
