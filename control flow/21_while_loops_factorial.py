# Find the factorial of a number using a while loop.
# A factorial of a whole number is that number multiplied by every whole number between itself and 1. For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.
# We can write a while loop to take any given number and figure out what its factorial is.

# number to find the factorial of
number = int(input("Input number: "))

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

print("Factorial")
print("n! = n.(n-1)!")

formula = "{} = {}".format(number,number,number,current)
# write your while loop here
while current < number:

    # multiply the product so far by the current number
    formula += ".({}-{})".format(number, current)
    product = product * (number - current)
    
    # increment current with each iteration until it reaches number
    current += 1

product = product * number
# print the factorial of number
print(formula)
print("Result:", product) 