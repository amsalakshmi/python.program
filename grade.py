students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("✅ Student added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for name, marks in students.items():
                if marks >= 90:
                    grade = "A"
                elif marks >= 75:
                    grade = "B"
                elif marks >= 50:
                    grade = "C"
                else:
                    grade = "Fail"
                print(f"{name} - Marks: {marks} - Grade: {grade}")

    elif choice == "3":
        print("👋 Exiting program...")
        break

    else:
        print("Invalid choice")