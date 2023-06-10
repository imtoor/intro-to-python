animals = {'dogs': [20,10,15,8,32,15], 'cats': [3,4,2,8,2,4], 'rabbits': [2,3,3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

#description
print("list: The data type of keys in the dictionary" )
print("15: animals['dogs'][-1] -> " + str(animals['dogs'][-1]))
# print("Error: " + str(animals[3]))
print("8: animals['dogs'][3] -> " + str(animals['dogs'][3]))
print("None: " + str(animals.get('chicken')))
print("string: " + str(type(animals.get("dogs"))))
print(animals.get("dogs"))
print(animals.get("fish"))