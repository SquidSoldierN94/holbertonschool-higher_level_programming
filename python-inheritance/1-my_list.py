#!/usr/bin/python3

class MyList(list):
    """
    MyList is a subclass of the built-in list class.
    
    This class inherits from the built-in list and provides 
    an additional method to print the list in a sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        
        The method uses the built-in sorted() function to create 
        a new sorted list from the original list and prints it.
        The original list remains unchanged.
        """
        print(sorted(self))  # Print the sorted version of the list
