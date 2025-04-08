class Phone:
    price = 19000
    color = 'color'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self):
        print('call one person')
    
    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text



my_phone = Phone()
print(my_phone.send_sms('Vivo', 'habijabi'))