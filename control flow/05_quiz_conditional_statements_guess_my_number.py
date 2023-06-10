# Guess the number

answer = 49
guest = 72

if answer < guest:
    result = "Oops! Your guess was too low."
elif answer > guest:
    result = "Oops! Your guess was too high."
elif answer == guest:
    result = "Nice! Your guess matched the answer!"

print(result)