points = 201
prize = ""
result = "Congratulations! You won a "
if points <= 50:
    prize = "wooden rabbit"
elif points <= 150:
    prize = "no prize"
elif points <= 180:
    prize = "wafer-thin mint"
elif points <= 200:
    prize = "penguin"
else:
    result = "Oh dear, no prize"
print(result + prize)