'''Comentário'''

lista = ["Lucas",26,1.71]
print(lista)

lista.append(2.6) #Insere um valor ao fim da lista
print(lista)

lista.pop() #Remove um valor da lista
            #Se não indicar qual posição ele irá remover o último
print(lista)
lista.pop(0) #Aqui foi indicado o índice 0
print(lista)

lista.insert(0, "Teste") #Permite inserir um valor na posição desejada
print(lista)
lista.pop(0)
print(lista)

nome = input("Digite o seu nome: ")
print("O nome digitado foi:",nome)

idade = int(input("Digite a sua idade: "))
if idade < 18:
    print("Você é menor de idade!")
else:
    print("Vocé é maior de idade!")




