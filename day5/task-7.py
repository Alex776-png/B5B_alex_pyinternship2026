class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, title):
        self.__books.append(title)

    def remove_book(self, title):
        if title in self.__books:
            self.__books.remove(title)
            print(f"'{title}' removed from the library.")
        else:
            print(f"'{title}' wasn't found in the library.")

    def list_books(self):
        if self.__books:
            print("Books in the library:")
            for book in self.__books:
                print("-", book)
        else:
            print("The library is empty.")


library = Library()

library.add_book("The Alchemist")
library.add_book("1984")
library.add_book("To Kill a Mockingbird")

library.list_books()

library.remove_book("1984")

library.list_books()