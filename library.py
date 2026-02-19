class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("✅ Book added successfully!\n")

    def view_books(self):
        if not self.books:
            print("No books in library.\n")
            return

        print("\n--- Library Books ---")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")
        print()

    def issue_book(self, index):
        if 0 <= index < len(self.books):
            if self.books[index].available:
                self.books[index].available = False
                print("✅ Book issued successfully!\n")
            else:
                print("❌ Book already issued!\n")
        else:
            print("Invalid book number!\n")

    def return_book(self, index):
        if 0 <= index < len(self.books):
            self.books[index].available = True
            print("✅ Book returned successfully!\n")
        else:
            print("Invalid book number!\n")


library = Library()

while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.view_books()
        num = int(input("Enter book number to issue: ")) - 1
        library.issue_book(num)

    elif choice == "4":
        library.view_books()
        num = int(input("Enter book number to return: ")) - 1
        library.return_book(num)

    elif choice == "5":
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Try again.\n")
