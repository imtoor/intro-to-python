# if else example
# n = 15

# if n % 2 == 0:
#     print("Number " + str(n) + " is even.")
# else:
#     print("Number " + str(n) + " is odd.") 

# if elif else example
# season = "fall"

# if season == "spring":
#     print("plant the garden!")
# elif season == "summer":
#     print("water the garden!")
# elif season == "fall":
#     print("harvest the garden!")
# elif season == "winter":
#     print("stay indoors!")
# else:
#     print("unrecognized season")

age = 28

# here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# these lines determine the bus fare prices
concession_tickets = 1.25
adult_ticket = 2.50

# here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_tickets
elif age >= senior_from_age:
    ticket_price = concession_tickets
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)