#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by any subclass.
        
        This method is intended to return the sound made by the animal.
        """
        pass

class Dog(Animal):
    
    def sound(self):
        """Returns the sound made by the dog."""
        return "Bark"

class Cat(Animal):
    
    def sound(self):
        """Returns the sound made by the cat."""
        return "Meow"
