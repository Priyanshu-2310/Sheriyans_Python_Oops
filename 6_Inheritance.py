class Parent: ## this is parent class or super class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"your name is {self.name} and age is {self.age}")

class Child(Parent): ## child class or subclass
    def __init__(self, name, age, email, password):
        super().__init__(name, age)
        self.email = email
        self.password = password
    
    def info(self):
        print(f"your name is = {self.name}\n your age is = {self.age}\n your email is = {self.email}\n your password = {self.password}")
        


obj = Parent("vinay", 48)
obj2 = Child("priyanshu", 22, "hello@gmail.com", 11111111)

obj2.info()
        