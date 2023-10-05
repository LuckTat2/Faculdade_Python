
print("MENU")
print("1 - Adicionar elemento ao topo da pilha")
print("2 - Remover um elemento do topo da pilha")
print("3 - Limpar pilha")
print("4 - Mostrar pilha")
print("5 - SAIR!")

pilha = []

opcao = int(input("Digite a sua opção: "))

while opcao != 5:
    if opcao == 1:
        valor = int(input("Digite um valor para adicionar à pilha: "))
        pilha.append(valor)
    elif opcao == 2:
        pilha.pop()
        if len(pilha) == 0:
            print("Pilha está vazia! Insira um valor")
    elif opcao == 3:
        pilha.clear()
    elif opcao == 4:
        print("Pilha atual:",pilha)
    else:
        print("Opção errada! Digite novamente")

    print("MENU")
    print("1 - Adicionar elemento ao topo da pilha")
    print("2 - Remover um elemento do topo da pilha")
    print("3 - Limpar pilha")
    print("4 - Mostrar pilha")
    print("5 - SAIR!")

    opcao = int(input("Digite sua opção: "))