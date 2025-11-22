class Registration:
    def __init__(self, name, age, number, blood):
        self.name = name
        self.age = age
        self.number = number
        self.blood = blood
        
    def show(self):
        print(f"Hello your name is {self.name}\nyour age is {self.age}\nyour number is {self.number}\nyour blood group is {self.blood}")

student1 = Registration("priyanshu", 12, 877232323, "B+")

student1.show()