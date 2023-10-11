from func import empilhar, desempilhar, limpar, mostrar, erro

print("MENU")
print("1 - Adicionar elemento ao topo da pilha")
print("2 - Remover um elemento do topo da pilha")
print("3 - Limpar pilha")
print("4 - Mostrar pilha")
print("5 - SAIR")

opcao = int(input("Digite a sua opção: "))

while opcao != 5:
    if opcao == 1:
        empilhar()
    elif opcao == 2:
        desempilhar()
    elif opcao == 3:
        limpar()
    elif opcao == 4:
        mostrar()
    else:
        erro()

    print("MENU")
    print("1 - Adicionar elemento ao topo da pilha")
    print("2 - Remover um elemento do topo da pilha")
    print("3 - Limpar pilha")
    print("4 - Mostrar pilha")
    print("5 - SAIR")

    opcao = int(input("Digite sua opção: "))