class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ ₹{amount} Deposited Successfully!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"✅ ₹{amount} Withdrawn Successfully!")

def main():
    atm = ATM(1000)  # Initial balance

    while True:
        print("\n🏧 ATM Menu")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))
            atm.withdraw(amount)

        elif choice == "4":
            print("👋 Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
