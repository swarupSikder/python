class Pen:
    man = 'Cho'

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def deal(self):
        text = f'{self.brand} {self.price}'
        return text
    
pen1 = Pen('Matador', 5)
print(pen1.brand)
