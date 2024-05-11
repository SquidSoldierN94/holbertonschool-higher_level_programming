#!/usr/bin/python3
def islower(c):
    for x in range(128):
        if x == ord(c):
            if 97 <= x < 123:  # Check if the character is lowercase
                print(f"{c} => lower")
            elif 65 <= x < 91:  # Check if the character is uppercase
                print(f"{c} => upper")
            break
