print("🗳 Mini Voting System")

candidates = {}
votes = {}

# Add candidates
num = int(input("Enter number of candidates: "))

for i in range(num):
    name = input(f"Enter candidate {i+1} name: ")
    candidates[i+1] = name
    votes[name] = 0

while True:
    print("\n1. Show Candidates")
    print("2. Cast Vote")
    print("3. Show Results")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n📋 Candidates List:")
        for key, value in candidates.items():
            print(f"{key}. {value}")

    elif choice == "2":
        vote = int(input("Enter candidate number to vote: "))
        if vote in candidates:
            candidate_name = candidates[vote]
            votes[candidate_name] += 1
            print("✅ Vote cast successfully!")
        else:
            print("❌ Invalid candidate number.")

    elif choice == "3":
        print("\n📊 Voting Results:")
        for name, count in votes.items():
            print(f"{name} : {count} votes")

        winner = max(votes, key=votes.get)
        print(f"\n🏆 Winner: {winner}")

    elif choice == "4":
        print("👋 Exiting Voting System!")
        break

    else:
        print("Invalid choice!")
