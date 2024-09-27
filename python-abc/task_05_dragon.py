#!/usr/bin/python3

class SwimMixin:
    """Mixin class to provide swimming functionality.

    This class adds the ability to swim to any class that inherits from it.
    """

    def swim(self):
        """Make the creature swim.

        This method prints a message indicating that the creature swims.
        """
        print("The creature swims!")

class FlyMixin:
    """Mixin class to provide flying functionality.

    This class adds the ability to fly to any class that inherits from it.
    """

    def fly(self):
        """Make the creature fly.

        This method prints a message indicating that the creature flies.
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon that can swim and fly.

    This class inherits functionality from SwimMixin and FlyMixin,
    allowing a dragon instance to both swim and fly.
    It also has its own unique behavior, such as roaring.
    """

    def roar(self):
        """Make the dragon roar.

        This method prints a message indicating that the dragon roars.
        """
        print("The dragon roars!")

if __name__ == "__main__":
    """Main entry point of the program.

    This block creates an instance of the Dragon class and demonstrates
    its abilities to swim, fly, and roar.
    """
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
