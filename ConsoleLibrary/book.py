class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "В наличии") -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return f"ID: {self.id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.id == other.id
                and self.title == other.title
                and self.author == other.author
                and self.year == other.year
                and self.status == other.status)
