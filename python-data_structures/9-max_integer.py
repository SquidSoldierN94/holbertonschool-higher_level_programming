#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    largest_number = my_list[0]
    for num in my_list:
        if num > largest_number:
            largest_number = num
    return largest_number
