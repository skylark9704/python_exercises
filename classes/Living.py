from abc import ABCMeta, abstractmethod

class Animal:

    __metaclass__ = ABCMeta

    legs = 0

    def __init__(self):
        pass

    @abstractmethod
    def type(self):
        pass
    
    @abstractmethod
    def can_speak(self):
        pass
    
    def num_legs(self):
        return self.legs


class Human(Animal):

    legs = 2

    def type(self):
        return "Human"
    
    def can_speak(self):
        return True

class Dog(Animal):

    legs = 4

    def type(self):
        return "Dog"

    def can_speak(self):
        return False

class Cat(Animal):

    legs = 4

    def type(self):
        return "Cat"

    def can_speak(self):
        return False
