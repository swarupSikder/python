# set: collection of unique items
numbers = [10, 96, 10, 67, 76, 10]
print(numbers)

numbers_set = set(numbers)
print(numbers_set)

# numbers_set.add(55)
# print(numbers_set)

# numbers_set.remove(10)
# print(numbers_set)

# for item in numbers_set:
#     print(item)

# if 9 in numbers_set:
#     print('exists')
# else:
#     print('not exists')


A = {1,3,5}
B = {1,2,3,4,5}
# intersection
print(A & B)

# union
print(A | B)