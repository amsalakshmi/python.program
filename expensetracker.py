import os

FILENAME = "expenses.txt"

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (Food/Travel/etc): ")

    with open(FILENAME, "a") as file:
        file.write(f"{amount},{category}\n")

    print("✅ Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses recorded yet.")
        return

    total = 0
    print("\n📋 Expense List:")
    with open(FILENAME, "r") as file:
        for line in file:
            amount, category = line.strip().split(",")
            print(f"₹{amount} - {category}")
            total += float(amount)

    print(f"\n💰 Total Expenses: ₹{total}")

while True:
    print("\n💸 Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("👋 Exiting Expense Tracker!")
        break
    else:
        print("Invalid choice! Try again.")
