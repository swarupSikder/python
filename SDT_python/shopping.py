class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def getCart(self):
        for item in self.cart:
            print(item)

    def add_to_cart(self, item, price, qty):
        product = {'item': item, 'price': price, 'qty': qty}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['qty']
        print('total price', total)
        if amount < total:
            print(f'Please provide {total-amount} more')
        else:
            extra = amount - total
            print(f'here is your extra money: {extra}')

    def remove_item(self, item):
        self.cart = [product for product in self.cart if product['item'] != item]


p1 = Shopping('koba sikder')
p1.add_to_cart('alu', 50, 6)
p1.add_to_cart('dim', 12, 24)
p1.add_to_cart('chaal', 50, 5)

p1.getCart()
p1.checkout(600)

p1.remove_item('alu')
p1.getCart()

