# number to find the factorial of
number = int(input("Input Number: "))

# start with our product equal to one
product = 1

formula = "{} = {}".format(number, number)

# write your for loop here
for current in range(1, number):

    formula += ".({}-{})".format(number, current)
    product = product * (number - current)

product = product * number

# print the factorial of number
print("Factorial")
print("n! = n.(n-1)!")
print(formula)
print("Result:", product)