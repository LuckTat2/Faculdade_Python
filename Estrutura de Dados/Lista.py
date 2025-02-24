lista = [1,2,3,4,5]

valor = lista[0]
print(valor)

lista.insert(0,0)
print(lista)

lista.remove(1)
print(lista)

lista[0] = 1
print(lista)

tamanho = len(lista)
print(tamanho)


lista = []

if not lista:
    print("A lista está vazia!")


lista = [1,2,3,4,5]

tamanho_maximo = 5
if len(lista) == 5:
    print("A lista está cheia!")
else:
    print("A lista não está cheia.")
