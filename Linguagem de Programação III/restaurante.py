class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self.produtos = []
        self.total = 0

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def somar_total(self):
        self.total = 0
        for produto in self.produtos:
            self.total += produto.preco
   
    def mostrar_resumo(self):
        print(f"Resumo do pedido número {self.numero}:")
        for produto in self.produtos:
            print(f"- {produto.nome}: R${produto.preco:.2f}")
        self.somar_total()
        print(f"Total do pedido: R${self.total:.2f}")

def main():
    produto1 = Produto("Hamburguer", 15.90)
    produto2 = Produto("Refrigerante", 7.50)
    produto3 = Produto("Batata Frita", 10.00)

    pedido1 = Pedido(1)
    pedido1.adicionar_produto(produto1)
    pedido1.adicionar_produto(produto2)
    pedido1.adicionar_produto(produto3)

    pedido1.mostrar_resumo()

if __name__ == "__main__":
    main()