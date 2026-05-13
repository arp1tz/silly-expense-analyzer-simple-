from datetime import date, datetime
import json
from unicodedata import category

def load_data():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except:
        return[]

def save_data(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)  

expenses = load_data()
# -------- FUNCTIONS --------

def add_expense(expenses):
    amount = int(input("Enter the amount spent: "))
    category = input("Enter the category: ").lower()
    expenses.append({
    'amount': amount,
    'category': category,
    'date': str(date.today())
})
    save_data(expenses)


def show_total(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print("Total expenses:", total)


def category_summary(expenses):
    category_totals = {}

    for exp in expenses:
        cat = exp['category']
        category_totals[cat] = category_totals.get(cat, 0) + exp['amount']

    total = sum(category_totals.values())

    print("\nCategory-wise expenses:")
    for cat, amt in category_totals.items():
        percent = (amt / total) * 100
        print(f"{cat}: {amt} ({percent:.2f}%)")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    print("\nAll Expenses:")

    for i, exp in enumerate(expenses, start=1):
           print(f"{i}. {exp['category']} - ₹{exp['amount']} on {exp.get('date', 'No Date')}")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete")
        return

    view_expenses(expenses)

    try:
        delete_index = int(input("\nEnter expense number to delete: "))

        if 1 <= delete_index <= len(expenses):
            removed = expenses.pop(delete_index - 1)

            save_data(expenses)

            print(f"Deleted: {removed['category']} - ₹{removed['amount']}")

        else:
            print("Invalid expense number")

    except ValueError:
        print("Please enter a valid number")

def edit_expense(expenses):
    if not expenses:
        print("No expenses to edit")
        return

    view_expenses(expenses)

    try:
        edit_index = int(input("\nEnter expense number to edit: "))

        if 1 <= edit_index <= len(expenses):

            new_amount = int(input("Enter new amount: "))
            new_category = input("Enter new category: ").lower()

            expenses[edit_index - 1]['amount'] = new_amount
            expenses[edit_index - 1]['category'] = new_category

            save_data(expenses)

            print("Expense updated successfully")

        else:
            print("Invalid expense number")

    except ValueError:
        print("Please enter valid input")
# -------- MAIN MENU --------

while True:
    print("\n1. Add Expense")
    print("2. View Total")
    print("3. Category Summary")
    print("4. View All Expenses")
    print("5. Edit Expense")
    print("6. Delete Expense")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        show_total(expenses)

    elif choice == "3":
        if expenses:
            category_summary(expenses)
        else:
            print("No expenses added yet")

    elif choice == "4":
        view_expenses(expenses)

    elif choice == "5":
        edit_expense(expenses)
    elif choice == "6":
        delete_expense(expenses)
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice")