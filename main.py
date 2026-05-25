import datetime
# DATA STORAGE

books = []
users = {}
issued_books = {}
# ADD BOOK
def add_book():

    book_id = input("Enter Book ID: ")

    # CHECK DUPLICATE ID
    for book in books:

        if book["id"] == book_id:
            print(" Book ID already exists.")
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)

    print(" Book added successfully!")
# VIEW BOOKS

def view_books():

    if len(books) == 0:
        print(" No books available.")
        return

    print("\n BOOK LIST")

    for book in books:

        status = "Available" if book["available"] else "Issued" #ternary operator 

        print(f"""
Book ID : {book['id']}
Title   : {book['title']}
Author  : {book['author']}
Status  : {status}
---------------------------
""")
# SEARCH BOOK

def search_book():

    keyword = input("Enter title to search: ").lower()

    found = False

    for book in books:

        if keyword in book["title"].lower():

            print(f"""
 Book Found
Book ID : {book['id']}
Title   : {book['title']}
Author  : {book['author']}
""")

            found = True

    if not found:
        print("Book not found.")

# DELETE BOOK


def delete_book():

    book_id = input("Enter Book ID to delete: ")

    for book in books:

        if book["id"] == book_id:

            books.remove(book)

            print(" Book deleted successfully!")
            return

    print("Book not found.")


# REGISTER USER


def register_user():

    username = input("Enter username: ")

    if username in users:
        print(" User already exists.")
        return

    password = input("Enter password: ")

    users[username] = {
        "password": password,
        "history": []
    }

    print(" User registered successfully!")

# ISSUE BOOK


def issue_book():

    username = input("Enter username: ")

    if username not in users:
        print(" User not found.")
        return

    book_id = input("Enter Book ID to issue: ")

    for book in books:

        if book["id"] == book_id:

            if not book["available"]:
                print("Book already issued.")
                return

            issue_date = datetime.date.today()
            due_date = issue_date + datetime.timedelta(days=7)

            book["available"] = False

            issued_books[book_id] = {
                "username": username,
                "issue_date": issue_date,
                "due_date": due_date
            }

            users[username]["history"].append(book["title"])

            print("Book issued successfully!")
            print(f"Due Date: {due_date}")

            return

    print(" Book not found.")

# RETURN BOOK

def return_book():

    book_id = input("Enter Book ID to return: ")

    if book_id not in issued_books:
        print(" This book was not issued.")
        return

    issue_info = issued_books[book_id]

    due_date = issue_info["due_date"]

    today = datetime.date.today()

    fine = 0

    if today > due_date:

        days_late = (today - due_date).days
        fine = days_late * 7

    for book in books:

        if book["id"] == book_id:
            book["available"] = True

    del issued_books[book_id]

    print(" Book returned successfully!")

    if fine > 0:
        print(f"Fine Amount: ₹{fine}")

# VIEW USER HISTORY

def user_history():

    username = input("Enter username: ")

    if username not in users:
        print(" User not found.")
        return

    history = users[username]["history"]

    print(f"\n Borrowing History of {username}")

    if len(history) == 0:
        print("No borrowing history.")

    else:

        for book in history:
            print(f" {book}")

# ADMIN REPORT


def admin_report():

    total_books = len(books)

    issued_count = len(issued_books)

    available_count = total_books - issued_count

    print("\n ADMIN DASHBOARD")

    print(f" Total Books     : {total_books}")
    print(f" Available Books : {available_count}")
    print(f" Issued Books    : {issued_count}")
    print(f" Total Users     : {len(users)}")


# MAIN MENU 

while True:

    print("""
LIBRARY MANAGEMENT SYSTEM


1. Add Book
2. View Books
3. Search Book
4. Delete Book
5. Register User
6. Issue Book
7. Return Book
8. User Borrowing History
9. Admin Dashboard
10. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        register_user()

    elif choice == "6":
        issue_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        user_history()

    elif choice == "9":
        admin_report()

    elif choice == "10":
        print(" Exiting Library System...")
        break

    else:
        print(" Invalid choice.")