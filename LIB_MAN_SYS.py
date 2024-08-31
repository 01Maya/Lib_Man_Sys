class Book:
    def __init__(self, isbn, title, author, year):
        """
        Initialize a new book.
        
        :param isbn: Unique identifier for the book (ISBN).
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Year the book was published.
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def __str__(self):
        """
        String representation of the book.
        """
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"'{self.title}' by {self.author} ({self.year}) - ISBN: {self.isbn} - Status: {status}"

class Library:
    def __init__(self):
        """
        Initialize the library with an empty dictionary of books.
        """
        self.books = {}

    def add_book(self, isbn, title, author, year):
        """
        Add a book to the library's collection.
        
        :param isbn: Unique identifier for the book (ISBN).
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Year the book was published.
        """
        if isbn in self.books:
            print(f"Error: A book with ISBN {isbn} already exists in the library.")
        else:
            self.books[isbn] = Book(isbn, title, author, year)
            print(f"Added '{title}' to the library.")

    def view_books(self):
        """
        View all available (not borrowed) books in the library.
        """
        available_books = [book for book in self.books.values() if not book.is_borrowed]
        if not available_books:
            print("No books available in the library.")
        else:
            print("Available books in the library:")
            for book in available_books:
                print(book)

    def borrow_book(self, isbn):
        """
        Borrow a book from the library.
        
        :param isbn: Unique identifier for the book (ISBN).
        """
        if isbn in self.books:
            book = self.books[isbn]
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
            else:
                print(f"Error: '{book.title}' is currently borrowed.")
        else:
            print(f"Error: No book found with ISBN {isbn}.")

    def return_book(self, isbn):
        """
        Return a borrowed book to the library.
        
        :param isbn: Unique identifier for the book (ISBN).
        """
        if isbn in self.books:
            book = self.books[isbn]
            if book.is_borrowed:
                book.is_borrowed = False
                print(f"Thank you for returning '{book.title}'.")
            else:
                print(f"Error: '{book.title}' was not borrowed.")
        else:
            print(f"Error: No book found with ISBN {isbn}.")

def main():
    """
    Main function to run the Library Management System.
    """
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Available Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            try:
                isbn = input("Enter ISBN: ").strip()
                title = input("Enter book title: ").strip()
                author = input("Enter author name: ").strip()
                year = int(input("Enter publication year: ").strip())
                library.add_book(isbn, title, author, year)
            except ValueError:
                print("Error: Publication year must be a valid integer.")
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            isbn = input("Enter ISBN of the book to borrow: ").strip()
            library.borrow_book(isbn)
        elif choice == '4':
            isbn = input("Enter ISBN of the book to return: ").strip()
            library.return_book(isbn)
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
