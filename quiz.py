questions = {
    "1. What is the capital of India? ": "delhi",
    "2. Which language is used for AI? ": "python",
    "3. 5 + 7 = ? ": "12",
    "4. Who developed Python? ": "guido",
}

score = 0

for question, answer in questions.items():
    user_answer = input(question).lower()

    if user_answer == answer:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")

print("\nQuiz Finished!")
print("Your Final Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent Performance! 🔥")
elif score >= 2:
    print("Good Job! 👍")
else:
    print("Keep Practicing! 💪")
