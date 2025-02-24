pilha = []
sair = "n"

while sair != "sair":
    valor = int(input("Digite um valor para adicionar à pilha: "))
    pilha.append(valor)
    sair = input("Deseja continuar: para sair digite 'sair'").lower()

print(pilha)

