class Cars:
    def __init__(self, color, price, wheel):
        self.color = color
        self.price = price
        self.wheel = wheel

    def showDetails(self):
        print(self.color)
        print(self.price)
        print(self.wheel)

Bmw = Cars("red", 400, 2)
print(Bmw.showDetails())
        