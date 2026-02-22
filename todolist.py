print("📋 Simple To-Do List")

FILE_NAME = "tasks.txt"

def show_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks yet.")

def add_task(task):
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")
    print("✅ Task added!")

def delete_task(task_number):
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(tasks)

            print("🗑️ Task deleted!")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print("No tasks to delete.")

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter new task: ")
        add_task(task)
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        delete_task(num)
    elif choice == "4":
        print("👋 Exiting To-Do List")
        break
    else:
        print("Invalid choice!")