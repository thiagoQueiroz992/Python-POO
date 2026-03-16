from rich import print

class Book():
    def __init__(self, book_name: str, pages: int):
        self.book_name = book_name
        self.pages = pages
        self.current_page = 1

    def advance_pages(self, pages = 1):
        pages_advanced = 0
        for p in range(pages):
            if pages_advanced == pages:
                print(f'Você avançou {pages_advanced} páginas e agora está na página {self.current_page}.')
                break
            else:
                self.current_page += 1
                pages_advanced += 1
                print(f'Página {self.current_page}')
        if self.current_page >= self.pages:
            print(f'Você chegou ao final do livro {self.book_name}')

book = Book('Teste', 20)
book.advance_pages(3)
book.advance_pages(5)
book.advance_pages()
book.advance_pages(30)