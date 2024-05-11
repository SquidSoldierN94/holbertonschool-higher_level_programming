#!/usr/bin/python3
def uppercase(str):
    lower = ''
    for char in str:
        if 'a' <= char <= 'z':
            str = chr(ord(char) - 32)
        else:
            lower = char
        str += lower
    print(f"{lower}")
