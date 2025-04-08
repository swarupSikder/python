class Calculator:
    brand = 'CASIO'
    def add(self, num1, num2):
        result = num1 + num2
        return result
    
    def deduct(self, num1, num2):
        result = num1 - num2
        return result
    
    def mult(self, num1, num2):
        result = num1 * num2
        return result
    
    def div(self, num1, num2):
        result = num1 / num2
        return result
    
myCalc = Calculator()
print(myCalc.add(40,20))
print(myCalc.deduct(40,20))
print(myCalc.mult(40,20))
print(myCalc.div(40,20))