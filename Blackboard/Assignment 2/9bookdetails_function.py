'''The following program asks user input for five books and
stores them in dictionary and
displays the input book data at the end'''

# Creation of an empty dictionary to hold data of 5 books
books = {}

# Loop to get details of 5 books
for i in range(1, 6):
    print("Enter details for Book", i)
    
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    cost = input("Cost: ")
    
    # Adding book details as a nested dictionary
    books[i] = {
        "Title": title,
        "Author": author,
        "ISBN": isbn,
        "Cost": cost
    }
    print() 

# Print all book details as output
print("Details of all 5 books:")
for book_id, details in books.items():
    print("Book", book_id)
    print("Title:", details["Title"])
    print("Author:", details["Author"])
    print("ISBN:", details["ISBN"])
    print("Cost:", details["Cost"])
    print()

# By Biplab Prasad Gajurel 25024641