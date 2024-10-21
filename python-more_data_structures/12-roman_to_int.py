#!/usr/bin/python3
def roman_to_int(roman_string):

    if not roman_string:
        if not isinstance(roman_string, str):
            return 0

    else:
        roman_dic = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000
            }

        number = 0
        prev_value = 0

    for char in reversed(roman_string):
        value = roman_dic[char]

        if value < prev_value:
            number -= value
        else:
            number += value

        prev_value = value

    return number
