class Veiculo:
    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        print("O carro está se movendo rápido.")

class Bicicleta(Veiculo):
    def mover(self):
        print("A bicicleta está se movendo devagar.")

def main():
    veiculo1 = Carro()
    veiculo2 = Bicicleta()

    veiculo1.mover()
    veiculo2.mover()

if __name__ == "__main__":
    main()