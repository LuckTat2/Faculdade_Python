class Carro:
    def __init__(self, marca, modelo, ano, cor): #Construtor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    #Métodos

    def buzinar(self):
        print("O carro ",self.modelo," buzinou!")
        
    def acelerar(self, incremento):
        self.velocidade += incremento
        return self.velocidade

    def frear(self, decremento):
        self.velocidade -= decremento
        if self.velocidade < 0:
            self.velocidade = 0
        return self.velocidade

    def mostrar_detalhes(self):
        print(f"Carro: {self.marca}, {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Velocidade: {self.velocidade} km/h")