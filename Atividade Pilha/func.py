pilha = []

def empilhar():
    valor = int(input("Digite um valor para adicionar à pilha: "))
    pilha.append(valor)

def desempilhar():
    if len(pilha) == 0:
        print("A pilha está vazia! Insira um valor")
    else:
        pilha.pop()

def limpar():
    pilha.clear()

def mostrar():
    print("Pilha atual:",pilha)

def erro():
    print("Opção inválida! Digite novamente")