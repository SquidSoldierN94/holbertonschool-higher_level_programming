#!/usr/bin/python3
for value in range(97, 123):
    if value not in range(101, 102) and value not in range(113, 114):
        print("{}".format(chr(value)), end='')
