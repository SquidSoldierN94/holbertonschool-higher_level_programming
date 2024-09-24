#!/usr/bin/python3

class MyList(list):
    """A class that inherits from list and adds a method to print sorted list."""

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
