print("📊 Student Grade Calculator")

name = input("Enter student name: ")

# Taking 5 subject marks
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

# Grade logic
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("\n----- Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
