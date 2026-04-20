amount = 90
category = "Petrol"

print(f"Amount: {amount}")
print(f"Category: {category}")


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


percent = (amount / total) * 100
print("Total expense:", total)
print(f"Percentage of {category} expense: {percent:.2f}%")