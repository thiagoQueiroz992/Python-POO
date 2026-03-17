from rich import print
from time import sleep

class Book():
    def __init__(self, book_name: str, pages: int):
        self.book_name = book_name
        self.pages = pages
        self.current_page = 1

        print(f':book: [blue]Você acabou de abrir o livro [green bold]\'{self.book_name}\'[/] que tem [red bold]{self.pages} páginas[/] no total. Você está na [yellow bold]página {self.current_page}[/].[/]')
        sleep(1)

    def advance_pages(self, pages = 1):
        print()
        for p in range(pages):
            self.current_page += 1
            print(f'Página {self.current_page}', end=' > ', flush=True)
            sleep(.5)
            if self.current_page == self.pages:
                break
        print(f'[blue]Você avançou [cyan bold]{p + 1} {'páginas' if p + 1 > 1 else 'página'}[/] e agora está na [yellow bold]página {self.current_page}[/].[/]', flush=True)
        sleep(1.2)
        if self.current_page == self.pages:
            print(f':closed_book: [red]Você chegou ao final do livro [bold]\'{self.book_name}\'[/].[/]')

book = Book('Teste', 20)
book.advance_pages(2)
book.advance_pages()
book.advance_pages(8)
book.advance_pages(11)
