state = "NY"
purchase_amount = 2500

if state == "CA":
    tax_amount = .075
elif state == "MN":
    tax_amount = .095
elif state == "NY":
    tax_amount = .089

total_cost = purchase_amount * (1 + tax_amount)
result = "Since you're from {}, your total cost is ${}.".format(state, total_cost)
print(result)