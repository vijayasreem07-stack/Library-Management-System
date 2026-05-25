print("hello world")
book = {
    "id": "101",
    "title": "Python Basics",
    "author": "John"
}

print(book)
print(book["title"])
#test loops 
books = ["Python", "C", "Java"]

for book in books:
    print(book)
#test conditions 
book_available = True

if book_available:
    print("Book can be issued")
else:
    print("Book already issued")
#test functions 
def greet():
    print("Welcome to Library")

greet()
#test  date system
import datetime

today = datetime.date.today()

due_date = today + datetime.timedelta(days=7)

print(today)
print(due_date)
