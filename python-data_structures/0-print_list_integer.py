#!/usr/bin/python3
def print_list_integer(my_list=None):
    if my_list is None:
        my_list = []
    for number in my_list:
        print("{}".format(number))
