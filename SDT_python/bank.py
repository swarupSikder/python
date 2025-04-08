class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        print(self.balance)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'Sorry! You cannot withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'Sorry! You cannot withdraw more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your balance after withdraw: {self.balance}')
        
# brac = Bank(15000)
# brac.withdraw(25)
# brac.withdraw(25000000)
# brac.withdraw(8700)


dbbl = Bank(10000)
dbbl.deposit(1500)
dbbl.deposit(600)
dbbl.get_balance()