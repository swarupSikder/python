# numbers = [12, 56, 98, 77, 6, 12, 98, 26]
# person = ['sikder', 'dhaka', 23, 'student']



# key value pair
# hash map
# object
# dictionary

person2 = {
    'name': 'sikder', 
    'address': 'dhaka', 
    'age': 23, 
    'profession': 'student'
}

# update a property
person2['name'] = 'koba'

# add new property
person2['skill'] = 'python'

# delete a property
del person2['age']

print(person2)
print(person2.keys())
print(person2.values())





# Additional Dictionary Looping
for k,v in person2.items():
    print(k,v)