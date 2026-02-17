import os

FILENAME = "account_data.txt"

def create_account():
    name = input("Enter your name: ")
    pin = input("Set 4-digit PIN: ")
    balance = 0

    with open(FILENAME, "w") as file:
        file.write(f"{name},{pin},{balance}\n")

    print("✅ Account created successfully!\n")


def load_account():
    if not os.path.exists(FILENAME):
        print("❌ No account found. Please create account first.\n")
        return None

    with open(FILENAME, "r") as file:
        data = file.readline().strip().split(",")

    return {"name": data[0], "pin": data[1], "balance": float(data[2])}


def save_account(account):
    with open(FILENAME, "w") as file:
        file.write(f"{account['name']},{account['pin']},{account['balance']}\n")


def transaction_history(message):
    with open("transactions.txt", "a") as file:
        file.write(message + "\n")


def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    save_account(account)
    transaction_history(f"Deposited: {amount}")
    print("✅ Deposit successful!\n")


def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        save_account(account)
        transaction_history(f"Withdrawn: {amount}")
        print("✅ Withdrawal successful!\n")
    else:
        print("❌ Insufficient balance!\n")


def check_balance(account):
    print(f"💰 Current Balance: {account['balance']}\n")


def view_transactions():
    if not os.path.exists("transactions.txt"):
        print("No transactions found.\n")
        return

    print("\n--- Transaction History ---")
    with open("transactions.txt", "r") as file:
        print(file.read())


while True:
    print("===== Advanced Banking System =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    main_choice = input("Enter choice: ")

    if main_choice == "1":
        create_account()

    elif main_choice == "2":
        account = load_account()
        if account:
            entered_pin = input("Enter PIN: ")
            if entered_pin == account["pin"]:
                print(f"Welcome {account['name']}!\n")

                while True:
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. View Transactions")
                    print("5. Logout")

                    choice = input("Enter choice: ")

                    if choice == "1":
                        deposit(account)
                    elif choice == "2":
                        withdraw(account)
                    elif choice == "3":
                        check_balance(account)
                    elif choice == "4":
                        view_transactions()
                    elif choice == "5":
                        print("Logging out...\n")
                        break
                    else:
                        print("Invalid choice!\n")
            else:
                print("❌ Wrong PIN!\n")

    elif main_choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid option!\n")
