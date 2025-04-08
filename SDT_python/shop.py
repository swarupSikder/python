class Shop:
    cart = []

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)

person1 = Shop('Koba Sikder')
person1.add_to_cart('shoe')
person1.add_to_cart('glass')
print(person1.cart)

person2 = Shop('Chitra')
person2.add_to_cart('cap')
person2.add_to_cart('watch')
print(person2.cart)