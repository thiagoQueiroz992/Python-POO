from rich import print

class Book():
    def __init__(self, book_name: str, pages: int):
        self.book_name = book_name
        self.pages = pages
        self.current_page = 1
