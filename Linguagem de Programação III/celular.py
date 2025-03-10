class Bateria():
    def __init__(self, capacidade):
        self.capacidade = capacidade

    def mostrar_detalhes(self):
        print(f"A bateria tem capacidade de {self.capacidade}mAh")

class Celular():
    def __init__(self, modelo, capacidade_bateria):
        self.modelo = modelo
        self.bateria = Bateria(capacidade_bateria)

    def mostrar_detalhes(self):
        print(f"O celular é do modelo {self.modelo} e tem uma bateria com capacidade de {self.bateria.capacidade}mAh")

def main():
    celular1 = Celular("Samsung Galaxy S21", 4000)
    celular1.mostrar_detalhes()
    celular1.bateria.mostrar_detalhes()

if __name__ == "__main__":
    main() 