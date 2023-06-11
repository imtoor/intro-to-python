weight = 55
height = 164

if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

is_raining = True
is_sunny = True
if is_raining and is_sunny:
    print("Is there a rainbow?")

not_unsubscribed = True
location = "NY"
if (not_unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")

# good and bad examples

# good
weather = "snow"
if weather == "snow" or weather == "rain":
    print("Wear boots!")

# bad
is_cold = False
if is_cold: # more readable than is_cold == True
    print("The weather is cold!")

correct_answer = False
if not correct_answer:
    print("That's incorrect - try again!")

# truth value testing
errors = 3
if errors:
    print("You have {} errors to fix!".format(errors))
else:
    print("No errors to fix!")