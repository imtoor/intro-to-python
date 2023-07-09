manifest = [
    ("bananas", 15),
    ("mattresses", 34),
    ("dog kennels", 42),
    ("machine", 120),
    ("cheeses", 5)
]

# items = ['bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses']
# weights = [15, 34, 42, 120, 5]
# print(list(zip(items, weights)))

# for item, weight in zip(items, weights):
#     print(item, weight)

print()

items, weights = zip(*manifest)
# print(item)
# print(weights)

# for i, item in zip(range(len(items)), items):
#     print(i, item)

for i, item in enumerate(items):
    print(i, item)
