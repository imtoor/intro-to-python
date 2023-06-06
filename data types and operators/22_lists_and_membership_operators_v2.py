greeting = "Hello there"
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

q3 = months[6:9]
print("q3: {}".format(q3))
first_half = months[:6]
print("first half: ", first_half)
second_half = months[6:]
print("second half: ", second_half)

print(len(greeting), len(months))
print(greeting[6:9], months[6:9])
#in and not in
print('her' in greeting, 'her' not in greeting)
print('Sunday' in months, 'Sunday' not in months)