class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}")

def main():
    livro1 = Livro("The Lord of the Rings", "J. R. R. Tolkien", "1954")
    livro2 = Livro("Game of Thrones", "George R. R. Martin", "1996")

    livro1.exibir_detalhes()
    livro2.exibir_detalhes()

if __name__ == "__main__":
    main()