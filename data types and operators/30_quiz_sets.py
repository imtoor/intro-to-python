# list to set
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
# print(a)
# print(b)
# print(len(a) - len(b))

# add and pop
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
print(b)