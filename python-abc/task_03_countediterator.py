#!/usr/bin/python3
class CountedIterator:
    """A custom iterator that counts the number of items iterated over.

    This class wraps an iterable and provides an interface to access its items while keeping track of how many items have been accessed.
    """

    def __init__(self, iterable):
        """Initialize the CountedIterator with the provided iterable.

        Args:
            iterable: An iterable (e.g., list, tuple, etc.) to create an iterator from.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return the next item from the iterator and increment the count.

        Returns:
            The next item from the iterable.

        Raises:
            StopIteration: If there are no more items to iterate over.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Get the current count of items that have been iterated over.

        Returns:
            int: The number of items accessed so far.
        """
        return self.count

    def __iter__(self):
        """Return the iterator object itself.

        This allows the CountedIterator instance to be used in a for loop or other contexts where an iterable is expected.

        Returns:
            CountedIterator: The iterator object itself.
        """
        return self
