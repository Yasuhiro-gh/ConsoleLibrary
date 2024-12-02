import argparse
import os
from .book import Book


def encode_book(book: Book):
    return book.__dict__


def is_book_exist(books: [Book], title: str, author: str, year: int) -> bool:
    for book in books:
        if book.title == title and book.author == author and book.year == year:
            return True
    return False


def init_storage(file_path: str) -> None:
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("[]")


def is_year_valid(year: str) -> bool:
    return year.isdigit() and 0 < int(year) < 2024


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ConsoleLibrary")
    parser.add_argument("-a", "--add", help="add book to library", action="store_true")
    parser.add_argument("-s", "--search", help="search book in library", action="store_true")
    parser.add_argument("-d", "--delete", help="delete book from library", action="store_true")
    parser.add_argument("-l", "--list", help="list books in library", action="store_true")
    parser.add_argument("-c", "--change", help="change book status", action="store_true")
    return parser
