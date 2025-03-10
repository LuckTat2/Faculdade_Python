class InstrumentoMusical:
    def tocar(self):
        pass

class Violao(InstrumentoMusical):
    def tocar(self):
        print("Tocando violão...")

class Piano(InstrumentoMusical):
    def tocar(self):
        print("Tocando piano...")

def main():
    instrumento1 = Violao()
    instrumento2 = Piano()

    instrumento1.tocar()
    instrumento2.tocar()

if __name__ == "__main__":
    main()