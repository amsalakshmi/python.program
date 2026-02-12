print("🔐 Simple Login System")

def register():
    username = input("Create username: ")
    password = input("Create password: ")

    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("✅ Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username and password == stored_password:
                print("🎉 Login successful!")
                return

        print("❌ Invalid username or password.")

    except FileNotFoundError:
        print("No users registered yet.")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice!")
