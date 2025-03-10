class Cliente():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class ContaBancaria():
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def exibir_saldo(self):
        print("O saldo atual é: {}".format(self.saldo))

def main():
    cliente1 = Cliente("Lucas", "085.544.324-24")
    conta1 = ContaBancaria(cliente1, 1980.54)

    print(f"O saldo do cliente {cliente1.nome} é de R${conta1.saldo:.2f}")

if __name__ == "__main__":
    main()