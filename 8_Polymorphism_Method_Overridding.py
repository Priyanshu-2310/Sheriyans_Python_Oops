class Animal:
    name = "lion"
    def speak(self):
        print("i roar")

class Dog(Animal):
    name = "tomy"
    def speak(self):
        print("I m barking")

lion = Animal()
dog = Dog()

lion.speak()
dog.speak()

