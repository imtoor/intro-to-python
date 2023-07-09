cities = ['makassar', 'maros', 'pangkep', 'barru', 'pare-pare', 'pinrang', 'polewali']
capitalized_cities = []
# for city in cities:
#     capitalized_cities.append(city.title())

capitalized_cities = [city.title() for city in cities]

print(capitalized_cities)

squares = [x**2 for x in range(9) if x % 2 == 0]

print(squares)

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

print(squares)

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

print(squares)
