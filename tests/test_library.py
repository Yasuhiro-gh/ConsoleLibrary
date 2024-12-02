import os
import unittest
from ConsoleLibrary.book import Book
from ConsoleLibrary.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library("test.json")

    def test_load_books(self):
        with open("test.json", "w") as file:
            file.write('''
            [
                {
                    "id": 0,
                    "title": "Book1",
                    "author": "Author1",
                    "year": 2001,
                    "status": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"
                },
                {
                    "id": 1,
                    "title": "Book2",
                    "author": "Author2",
                    "year": 2002,
                    "status": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"
                },
                {
                    "id": 2,
                    "title": "Book3",
                    "author": "Author3",
                    "year": 2003,
                    "status": "\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"
                }
            ]
            ''')

        book1 = Book(0, "Book1", "Author1", 2001)
        book2 = Book(1, "Book2", "Author2", 2002)
        book3 = Book(2, "Book3", "Author3", 2003)

        self.assertListEqual(self.lib.get_books(), [book1, book2, book3], "Books load work incorrect")

    def test_add_book(self):
        self.lib.add_book("Book1", "Author1", 2001)
        book = Book(0, "Book1", "Author1", 2001)

        self.assertEqual(self.lib.get_books(), [book], "Books add work incorrect")

        with self.assertRaises(ValueError) as cm:
            self.lib.add_book("Book1", "Author1", 2001)
        self.assertTrue('Book with title Book1, author Author1 and year 2001 already exist' in cm.exception.__str__(),
                        "Possible to add same book")

    def test_remove_book(self):
        self.lib.add_book("Book1", "Author1", 2001)
        self.lib.add_book("Book2", "Author2", 2002)
        self.lib.add_book("Book3", "Author3", 2003)
        book1 = Book(0, "Book1", "Author1", 2001)
        book3 = Book(2, "Book3", "Author3", 2003)
        self.lib.delete_book(1)

        self.assertEqual(self.lib.get_books(), [book1, book3], "Books remove work incorrect")

        with self.assertRaises(ValueError) as cm:
            self.lib.delete_book(1)
        self.assertTrue('Book with id 1 not found' in cm.exception.__str__(),
                        "Possible to remove nonexistent book")

    def test_search_book(self):
        self.lib.add_book("Book1", "Author1", 2001)
        self.lib.add_book("Book2", "Author2", 2002)
        self.lib.add_book("Book3", "Author3", 2003)

        book1 = Book(0, "Book1", "Author1", 2001)
        book2 = Book(1, "Book2", "Author2", 2002)
        book3 = Book(2, "Book3", "Author3", 2003)

        self.assertListEqual(self.lib.search_books(title="Book2"), [book2],
                             "Search books by title work incorrect")
        self.assertListEqual(self.lib.search_books(author="Author2"), [book2],
                             "Search books by author work incorrect")
        self.assertListEqual(self.lib.search_books(year="2002"), [book2],
                             "Search books by year work incorrect")
        self.assertListEqual(self.lib.search_books(title="Book2", author="Author2", year="2002"), [book2],
                             "Search books by parameters work incorrect")
        self.assertListEqual(self.lib.search_books(author="author4"), [], "Search nonexistent book")
        self.assertListEqual(self.lib.search_books(), [book1, book2, book3],
                             "Search books with empty parameters work incorrect")

    def test_change_status(self):
        self.lib.add_book("Book1", "Author1", 2001)
        self.lib.change_book_status(0, "Выдана")
        self.assertEqual(self.lib.get_books()[0].status, "Выдана", "Change book status work incorrect")
        with self.assertRaises(ValueError) as cm:
            self.lib.change_book_status(1, "Выдана")
        self.assertTrue('Book with id 1 not found' in cm.exception.__str__(),
                        "Possible to change status of nonexistent book")

    def __del__(self):
        if os.path.exists("test.json"):
            os.remove("test.json")


if __name__ == '__main__':
    unittest.main()
