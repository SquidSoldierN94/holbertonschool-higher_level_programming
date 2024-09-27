#!/usr/bin/python3

class Fish:
    """A class representing a fish.

    This class provides basic functionalities related to fish behavior and habitat.
    """

    def swim(self):
        """Make the fish swim.

        This method prints a message indicating that the fish is swimming.
        """
        print("The fish is swimming")
    
    def habitat(self):
        """Describe the habitat of the fish.

        This method prints a message indicating that the fish lives in water.
        """
        print("The fish lives in water")

class Bird:
    """A class representing a bird.

    This class provides basic functionalities related to bird behavior and habitat.
    """

    def fly(self):
        """Make the bird fly.

        This method prints a message indicating that the bird is flying.
        """
        print("The bird is flying")
    
    def habitat(self):
        """Describe the habitat of the bird.

        This method prints a message indicating that the bird lives in the sky.
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """A class representing a flying fish, which inherits from both Fish and Bird.

    This class overrides methods from both parent classes to provide specialized behavior
    for the flying fish, which can swim and fly.
    """

    def swim(self):
        """Make the flying fish swim.

        This method overrides the swim method from the Fish class and prints a message 
        indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")
    
    def fly(self):
        """Make the flying fish fly.

        This method overrides the fly method from the Bird class and prints a message 
        indicating that the flying fish is soaring.
        """
        print("The flying fish is soaring!")
    
    def habitat(self):
        """Describe the habitat of the flying fish.

        This method overrides the habitat methods from both the Fish and Bird classes 
        to indicate that the flying fish lives both in water and in the sky.
        """
        print("The flying fish lives both in water and the sky!")

if __name__ == "__main__":
    """Main entry point of the program.

    This block creates an instance of the FlyingFish class, calls its methods to 
    demonstrate its capabilities, and prints the method resolution order (MRO).
    """
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    
    print(FlyingFish.mro())
