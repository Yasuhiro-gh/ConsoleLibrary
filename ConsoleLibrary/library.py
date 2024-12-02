import json
from .book import Book
from .utils import encode_book, is_book_exist, init_storage


class Library:
    def __init__(self, path: str):
        init_storage(path)
        self.file_path = path
        self.books: list[Book] = []
        self.__load_books()

    def __load_books(self) -> None:
        """
        Load books from json file
        """
        try:
            with open(self.file_path, 'r') as f:
                books: list[Book] = []
                for json_book in json.load(f):
                    books.append(Book(**json_book))
                self.books = books
        except FileNotFoundError:
            print("JSON file missing or creating")

    def __update_books(self) -> None:
        """
        Update books in json file
        """
        with open(self.file_path, 'w') as f:
            json.dump(self.books, f, indent=4, default=encode_book)

    def __create_book(self, title: str, author: str, year: int) -> Book:
        new_id = 0
        if len(self.books) > 0:
            new_id = self.books[-1].id + 1
        return Book(new_id, title, author, year)

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Add a book to the library

        Args:
            title (str): Title of the book
            author (str): Author of the book
            year (int): Year of the book
        """
        if is_book_exist(self.books, title, author, year):
            raise ValueError(f"Book with title {title}, author {author} and year {year} already exist")
        book = self.__create_book(title, author, year)
        self.books.append(book)
        self.__update_books()
        print(f"Book `{book.title}` by {book.author}, {book.year} was added")

    def delete_book(self, book_id: int) -> None:
        """
        Delete a book from the library

        Args:
            book_id (int): ID of the book

        Returns:
            Book
        """
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.__update_books()
                print(f"Book `{book.title}` by {book.author}, {book.year} was successfully deleted")
                break
        else:
            raise ValueError(f"Book with id {book_id} not found")

    def search_books(self, title: str = "", author: str = "", year: str = "") -> list[Book]:
        """
        Search books in library

        Args:
            title (str, optional): Title of the book. Defaults to "".
            author (str, optional): Author of the book. Defaults to "".
            year (str, optional): Year of the book. Defaults to "".

        Returns:
            Filtered list of books. If arguments empty, return all books.
        """
        self.__load_books()
        books: list[Book] = self.books
        if title:
            books = list(filter(lambda book: book.title == title, books))
        if author:
            books = list(filter(lambda book: book.author == author, books))
        if year:
            books = list(filter(lambda book: book.year == int(year), books))
        return books

    def get_books(self) -> list[Book]:
        """
        Return all books from the library

        Returns:
            list[Book]
        """
        self.__load_books()
        return self.books

    def change_book_status(self, book_id: int, status: str) -> None:
        """
        Change the status of a book

        Args:
            book_id (int): ID of the book
            status (str): new status of the book
        """
        for book in self.books:
            if book.id == book_id:
                book.status = status
                self.__update_books()
                print(f"Status of the book `{book.title}` was successfully changed to `{status}`")
                break
        else:
            raise ValueError(f"Book with id {book_id} not found")
