'''The following program inputs book deatils of library using
Object Oriented Programming and file handling concept and 
also, the data is stored for easy access to modify and to view the contents'''

import os

# Defining a class called Book for book details
class Book:
    def __init__(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued  # True or False

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")

    def to_line(self):
        # Conversion of book info to a line for file storage
        return f"{self.book_id}|{self.title}|{self.author}|{self.is_issued}\n"

    @staticmethod
    def from_line(line):
        # Creation of Book object from a line in file
        parts = line.strip().split('|')
        book_id = parts[0]
        title = parts[1]
        author = parts[2]
        is_issued = parts[3] == 'True'
        return Book(book_id, title, author, is_issued)


class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        self.books = []
        if not os.path.exists(self.filename):
            # If file doesn't exist, starting with empty list
            return
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if line.strip():
                        book = Book.from_line(line)
                        self.books.append(book)
        except Exception as e:
            print(f"Error loading books from file: {e}")

    def save_books(self):
        try:
            with open(self.filename, 'w') as f:
                for book in self.books:
                    f.write(book.to_line())
        except Exception as e:
            print(f"Error saving books to file: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Book '{book.title}' added to library.")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def issue_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            if book.is_issued:
                print(f"Book '{book.title}' is already issued.")
            else:
                book.is_issued = True
                self.save_books()
                print(f"Book '{book.title}' has been issued.")
        else:
            print("Book not found.")

    def return_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            if not book.is_issued:
                print(f"Book '{book.title}' is not issued currently.")
            else:
                book.is_issued = False
                self.save_books()
                print(f"Book '{book.title}' has been returned.")
        else:
            print("Book not found.")

    def search_books(self, search_term):
        found = [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.book_id.lower()]
        if not found:
            print("No books found matching your search.")
        else:
            print(f"\nFound {len(found)} book(s):")
            for book in found:
                book.display()

    def display_all_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\n--- Library Books ---")
            for book in self.books:
                book.display()

# The main program with OOP concepts
def main():
    library = Library()

    while True:
        print("\nLibrary Management Menu:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Display All Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            new_book = Book(book_id, title, author)
            library.add_book(new_book)

        elif choice == '2':
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == '3':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '4':
            search_term = input("Enter Book Title or ID to search: ")
            library.search_books(search_term)

        elif choice == '5':
            library.display_all_books()

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# by Biplab Prasad Gajurel 25024641