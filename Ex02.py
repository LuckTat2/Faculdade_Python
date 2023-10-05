pilha=[1,8,"Teste"]

if len(pilha)==0:
    print("Pilha vazia, não é possível remover valores")
else:
    print(pilha)
    pilha.pop()
    print(pilha)

pilha2 = [85.9, "Aluno", 45]
print(pilha2[-1]) #Se o índice for -1, acessamos o último valor da pilha

pilha2.clear() #Limpa pilha

lenI(pilha2) #Retorna a quantidade de elementos da pilha
sum(pilha2) #Soma os elementos da pilha
max(pilha2) #Retorna o maior valor
min(pilha2) #Retorna o menor valor



