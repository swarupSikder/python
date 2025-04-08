class Phone:
    manufactured = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    
    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone}, {sms}'
        return text



my_phone = Phone('koba', 'iPhone', 3600)
her_phone = Phone('Chitra', 'iPhone', 8700)

print(my_phone.owner, my_phone.brand, my_phone.price)
print(her_phone.owner, her_phone.brand, her_phone.price)