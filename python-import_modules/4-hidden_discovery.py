#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith("__")]  # Filter out names starting with __
    for name in sorted(filtered_names):
        print(name)
