countries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark', 'Sweden', 'Ghana']
country_set = set(countries)
# print('India' in countries)
# print('India' in country_set)
country_set.add('Italy')
# print(country_set)

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

fruit = {"apple", "banana", "orange", "grapefruit"}
print(fruit)
print("watermelon" in fruit)
fruit.add("watermelon")
print("watermelon" in fruit)
print(fruit.pop())
print(fruit)