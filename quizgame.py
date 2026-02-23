print("🎲 Simple Quiz Game")

questions = {
    "1. What is the capital of India?": "delhi",
    "2. What is 5 + 7?": "12",
    "3. Which language is used for AI mostly?": "python",
    "4. What is the largest planet?": "jupiter",
    "5. How many days in a week?": "7"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ").lower()
    
    if user_answer == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {answer}\n")

print("🎯 Quiz Finished!")
print(f"Your Final Score: {score} / {len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage}%")

if percentage >= 80:
    print("🏆 Excellent!")
elif percentage >= 50:
    print("👍 Good Job!")
else:
    print("📚 Need More Practice!")
