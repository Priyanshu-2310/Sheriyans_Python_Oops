from abc import ABC , abstractmethod

class Animal:
    @abstractmethod
    def speak():
        pass


class Dog(Animal):
    def speak(self):
        print("I m dog")


dog = Dog()
dog.speak()
