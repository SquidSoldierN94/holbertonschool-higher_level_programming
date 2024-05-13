#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_element_a = tuple_a[0] if len(tuple_a) >= 1 else 0
    first_element_b = tuple_b[0] if len(tuple_b) >= 1 else 0
    second_element_a = tuple_a[1] if len(tuple_a) >= 2 else 0
    second_element_b = tuple_b[1] if len(tuple_b) >= 2 else 0
    result_first_element = first_element_a + first_element_b
    result_second_element = second_element_a + second_element_b
    return (result_first_element, result_second_element)
