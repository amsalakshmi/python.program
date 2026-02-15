import random

print("✊ Rock 🖐 Paper ✌ Scissors Game")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("\nEnter rock/paper/scissors (or 'exit' to quit): ").lower()

    if user == "exit":
        print("👋 Game Over!")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie! 🤝")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You win this round!")
        user_score += 1

    else:
        print("💻 Computer wins this round!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")

print(f"\n🏆 Final Score → You: {user_score} | Computer: {computer_score}")
