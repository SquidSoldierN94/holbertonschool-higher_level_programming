#!/usr/bin/python3
import sys
def main():
    argv = sys.argv
    num_args = len(argv) - 1
    total = 0
    if num_args == 0:
        print("0")
    for i in range(1, num_args + 1):
        total += int(argv[i])
        print(total)
if __name__ == "__main__":
    main()
