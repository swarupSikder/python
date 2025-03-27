# lamb da

# def doubled(x):
#     return x*2

doubled = lambda num: num*2
squared = lambda num: num*num
addNums = lambda x,y: x+y

# print(doubled(44))
# print(squared(44))
# print(addNums(45, 56))








# numbers = [12, 56, 98, 77, 6, 12, 98, 26]
# doubled_nums = map(doubled, numbers)
# squared_nums = map(lambda x: x**2, numbers)

# print(numbers)
# print(list(doubled_nums))
# print(list(squared_nums))








actors = [
    {'name': 'swarup', 'age': 28},
    {'name': 'sikder', 'age': 23},
    {'name': 'koba', 'age': 38},
    {'name': 'sarah', 'age': 65},
    {'name': 'chitra', 'age': 17},
]

juniors = filter(lambda actor: actor['age'] < 30, actors)
print(list(juniors))