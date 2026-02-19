import random

print("🎲 Dice Rolling Simulator")

roll_history = []

while True:
    print("\n1. Roll Dice")
    print("2. View Roll History")
    print("3. View Statistics")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = random.randint(1, 6)
        roll_history.append(roll)
        print(f"🎲 You rolled: {roll}")

    elif choice == "2":
        if roll_history:
            print("📜 Roll History:", roll_history)
        else:
            print("No rolls yet.")

    elif choice == "3":
        if roll_history:
            print("📊 Statistics:")
            print("Total Rolls:", len(roll_history))
            print("Highest Roll:", max(roll_history))
            print("Lowest Roll:", min(roll_history))
            print("Average Roll:", sum(roll_history)/len(roll_history))
        else:
            print("No data available.")

    elif choice == "4":
        print("Exiting Dice Simulator 🎲")
        break

    else:
        print("Invalid choice! Try again.")
