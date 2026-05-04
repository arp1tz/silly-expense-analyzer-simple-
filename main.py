
expenses = []

def add_expenses(expenses):
   amount = int(input("Enter the amount spent: "))
   category = input("Enter the category of the expense: ")
   expenses.append({'amount': amount, 'category': category})

def show_total(expenses):
   total = sum(exp['amount'] for exp in expenses)
   print("Total expenses: ", total)

def category_summary(expenses):
    category_totals = {}

    for exp in expenses:
        cat = exp['category']
        category_totals[cat] = category_totals.get(cat, 0) + exp['amount']

    total = sum(category_totals.values())

    print("\nCategory-wise expenses:")
    for cat, amt in category_totals.items():
    

while True:
    amount = int(input("Enter the amount spent: "))
    category = input("Enter the category of the expense: ")

    expenses.append({'amount': amount, 'category': category})

    choice = input("Do you want to add another expense? (yes/no): ")
    if choice == "no":
       break
    

total = 0
for expense in expenses:
  total += expense["amount"]
print("Total expenses: ", total)

category_totals = {}

for expense in expenses:
   cat = expense["category"]

   if cat in category_totals:
      category_totals[cat] += expense ["amount"]
   else:      category_totals[cat] = expense["amount"]
print("\nCategory-wise expenses:")

for cat, amount in category_totals.items():
    print(cat, ":", amount)

if total > 1000:
    print("⚠️ You are spending too much!")
else:
    print("✅ Spending is under control")

percent = (amount / total) * 100
print(f"\nPercentage of total expenses: {percent:.2f}%")
