#!/usr/bin/python3

class VerboseList(list):

    def append(self, item):
        """Add an item to the end of the list and print a notification message.
        
        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """Extend the list by appending elements from the iterable and print a notification message.
        
        Args:
            iterable: An iterable (e.g., list, tuple) whose elements will be added to the list.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")
    
    def remove(self, item):
        """Remove the first occurrence of the item from the list and print a notification message.
        
        Args:
            item: The item to be removed from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Remove and return the item at the given index (default is the last item) and print a notification message.
        
        Args:
            index (int, optional): The index of the item to be removed. Default is -1 (the last item).
        
        Returns:
            The item that was removed.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
