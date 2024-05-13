#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_cpy = [x for x in my_list]
    if idx < 0 or idx >= len(my_list_cpy):
        return my_list_cpy
    else:
        my_list_cpy[idx] = element
        return my_list_cpy
