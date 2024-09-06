#!/usr/bin/python3
import sys
if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_args = len(arguments)
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")
    for index, arg in enumerate(arguments, start=1):
        print(f"{index}: {arg}")
