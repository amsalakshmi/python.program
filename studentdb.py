import sqlite3

print("🗄 SQLite Student Management System")

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    mark INTEGER
)
""")
conn.commit()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    mark = int(input("Enter mark: "))

    cursor.execute("INSERT INTO students (name, age, mark) VALUES (?, ?, ?)", (name, age, mark))
    conn.commit()
    print("✅ Student added!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if rows:
        print("\n📋 Student Records:")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Mark: {row[3]}")
    else:
        print("No records found.")

def update_student():
    student_id = int(input("Enter student ID to update: "))
    new_mark = int(input("Enter new mark: "))

    cursor.execute("UPDATE students SET mark=? WHERE id=?", (new_mark, student_id))
    conn.commit()

    if cursor.rowcount:
        print("✏ Updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()

    if cursor.rowcount:
        print("🗑 Deleted successfully!")
    else:
        print("Student not found.")


while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student Mark")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("👋 Exiting Database System!")
        break
    else:
        print("Invalid choice!")

conn.close()
