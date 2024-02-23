# i.py - Interface Segregation Principle (ISP) Example
# A client should never be forced to implement an interface that it doesn’t use, or clients shouldn’t be forced to depend on methods they do not use.

from abc import ABC, abstractmethod

# Interfaces for different types of users
class GuestUserInterface(ABC):
    @abstractmethod
    def search_books(self, query):
        pass

class LibrarianInterface(ABC):
    @abstractmethod
    def search_books(self, query):
        # Implement logic for searching books
        pass
    
    @abstractmethod
    def add_book(self, book):
        # Implement logic for adding books
        pass
    
    @abstractmethod
    def remove_book(self, book):
        # Implement logic for removing books
        pass
    
    @abstractmethod
    def generate_reports(self):
        # Implement logic for generating reports
        pass

class RegisteredUserInterface(ABC):
    @abstractmethod
    def search_books(self, query):
        pass
    
    @abstractmethod
    def borrow_book(self, book):
        pass
    
    @abstractmethod
    def return_book(self, book):
        pass

# Implementing concrete classes for each type of user
class GuestUser(GuestUserInterface):
    def search_books(self, query):
        print("Guest user searching for books with query:", query)

class Librarian(LibrarianInterface):
    def search_books(self, query):
        print("Librarian searching for books with query:", query)
    
    def add_book(self, book):
        print("Adding book to the catalog:", book)
    
    def remove_book(self, book):
        print("Removing book from the catalog:", book)
    
    def generate_reports(self):
        print("Generating reports")

class RegisteredUser(RegisteredUserInterface):
    def search_books(self, query):
        print("Registered user searching for books with query:", query)
    
    def borrow_book(self, book):
        print("Borrowing book:", book)
    
    def return_book(self, book):
        print("Returning book:", book)

def main():
    guest_user = GuestUser()
    librarian = Librarian()
    registered_user = RegisteredUser()
    
    # Guest user functionality
    guest_user.search_books("Software Enineering 101")
    
    # Librarian functionality
    librarian.search_books("The Hunger Games")
    librarian.add_book("Introduction to HTML")
    librarian.generate_reports()
    
    # Registered user functionality
    registered_user.search_books("The Outsiders")
    registered_user.borrow_book("Algorithms 101")
    registered_user.return_book("Game Theory 101")

if __name__ == "__main__":
    main()
