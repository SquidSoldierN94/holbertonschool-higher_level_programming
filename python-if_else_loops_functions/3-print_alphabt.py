#!/usr/bin/python3
for ascii_value in range(97, 123):
    if ascii_value not in range(101, 102) and ascii_value not in range(113, 114):
        print(chr(ascii_value), end='')
