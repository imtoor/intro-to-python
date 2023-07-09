limit = 75

# Mine
square_num = 1
nearest_square = 0
# write your while loop here
while square_num < limit:
    if (square_num * square_num) > limit:
        square_num = square_num - 1
        nearest_square = square_num * square_num
        break
    print("{} x {} : {}".format(square_num, square_num, square_num * square_num))
    square_num += 1

# Tutorial
num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)