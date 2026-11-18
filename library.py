book_name = "Python Programming"
author = "Guido van Rossum"
price = 450

print("LIBRARY MANAGEMENT SYSTEM")
print("Book Name:", book_name)
print("Author:", author)
print("Price: Rs.", price)
def issue_book():
    book_name = input("Enter book name to issue: ")
    print(book_name, "has been issued successfully!")

issue_book()