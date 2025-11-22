class Animal:
    Gender = "Male", ## this is class attributes
    def __init__(self, name, age): ## this is instance method
        self.name = name
        self.age = age

    def info(self): ## this is also instance method
        print("This is instance method")
    
    @classmethod
    def clsmethod(cls):  ## cls pe animal class aa rhi hai
        print(cls.Gender)

    @staticmethod
    def static():
        print("I m static method")


obj = Animal("Lion", 11)
obj.info()
obj.clsmethod()
        