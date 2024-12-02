from ConsoleLibrary.library import Library
from ConsoleLibrary.utils import create_parser, is_year_valid


def run():
    lib = Library("books.json")
    parser = create_parser()
    args = parser.parse_args()

    if args.add:
        print("To add the book please provide info")
        title = input("Insert book title: ").strip()
        author = input("Insert book author: ").strip()
        year = input("Insert book year: ").strip()
        while not is_year_valid(year):
            year = input("Please enter a valid year: ")
        year = int(year)
        lib.add_book(title, author, year)
    elif args.search:
        print("To search the book please provide title, author or year")
        title = input("Insert book title: ").strip()
        author = input("Insert book author: ").strip()
        year = input("Insert book year: ").strip()
        if year != "":
            while not is_year_valid(year):
                year = input("Please enter a valid year: ")
        books = lib.search_books(title, author, year)
        for book in books:
            print(book)
    elif args.delete:
        print("To delete the book please provide id: ")
        book_id = input("Insert book id: ").strip()

        while not book_id.isdigit():
            book_id = input("Please enter a valid id: ")

        book_id = int(book_id)
        lib.delete_book(book_id)
    elif args.list:
        for book in lib.get_books():
            print(book)
    elif args.change:
        print("To change book status please provide id and choose status: ")
        book_id = input("Insert book id: ").strip()
        while not book_id.isdigit():
            book_id = input("Please enter a valid id: ").strip()
        book_id = int(book_id)
        print("1: В наличии")
        print("2: Выдана")
        status_number = input("Please enter your choice: ").strip()
        while status_number not in ["1", "2"]:
            status_number = input("Please enter 1 or 2: ")
        status = "В наличии"
        if status_number == "2":
            status = "Выдана"
        lib.change_book_status(book_id, status)
    else:
        parser.print_help()
