class Factory:
    a = "hello I am an attribute"
    def hello():
        print("I am a method")

obj = Factory()

print(obj) ## it give the location of Factory class
print(obj.a)
print(obj.hello()) ## it give us error because class ke ander jo hello method hai waha pe ek argument jata hai jo obj object hoga