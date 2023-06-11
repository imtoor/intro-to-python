cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

# for city in cities:
#     print("City is {}".format(city))

print("")

capitalize_cities = []

for city in cities:
    capitalize_cities.append(city.title())

# for capCity in capitalize_cities:
#     print("Capitalize city is {}".format(capCity))

print(list(range(4))) # to stop range
print(list(range(2, 6))) # from start to stop range
print(list(range(1, 10, 2))) # from start to stop and incremented by 2

print(range(4))

for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)

for i in range(3):
    print("Hello!")