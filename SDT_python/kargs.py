def full_name(first, last):
    name = f'{first} {last}'
    return name

# maintaining order
# name = full_name('Swarup', 'Sikder')

# no order
name = full_name(last='Sikder', first='Swarup')

#print
print(name)
print('-------------')







# (**kargs)

def famous_name(first, last, **additional):
    name = f'{additional['title1']} {first} {last}'

    # print(additional)

    for key, value in additional.items():
        print(key, value)

    return name

# name = famous_name(first='Swarup', last='Sikder', title='Mr', additional='Banker')
name = famous_name(first='Swarup', last='Sikder', title1='Mr', title2='Master')
print(name)
print('-------------')











def a_lot(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    rem = num1 % 2
    # return [sum, mul, rem]    #return as a list
    return sum, mul, rem        #return as a tuple

everything = a_lot(55, 21)
print(everything)