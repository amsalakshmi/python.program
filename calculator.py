print("🧮 Simple Calculator")

while True:
    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Calculator closed.")
        break

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", num1 + num2)

        elif choice == '2':
            print("Result:", num1 - num2)

        elif choice == '3':
            print("Result:", num1 * num2)

        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid input! Please select 1-5.")
