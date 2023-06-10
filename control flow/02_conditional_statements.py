phone_balance = 8
bank_balance = 100

print("before")
print("phone_balance: " + str(phone_balance) + "\nbank_balance: " + str(bank_balance))

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print("\nafter")
print("phone_balance: " + str(phone_balance) + "\nbank_balance: " + str(bank_balance))