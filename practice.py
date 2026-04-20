expenses = []
amount = 100
category = "food"
expenses.append({"amount": amount, "category": category})
expenses.append({"amount": 50, "category": "transport"})
expenses.append({"amount": 200, "category": "transport"})
print(expense)

total = 0

for expense in expenses:
    total += expense["amount"]

print("Total expense:", total)