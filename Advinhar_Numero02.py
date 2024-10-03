import random

print("O número secreto está entre 1 e 10!")

tentativas = 0
num = 0
num_secreto = random.randint(1,10)

while tentativas < 3:
        num = int(input("Advinhe o número: "))
        if num == num_secreto:
            print("Parabéns, você acertou!")
            break
        elif num > num_secreto:
             print("Muito alto!")
             tentativas += 1
        elif num < num_secreto:
             print("Muito baixo!")
             tentativas += 1
                
print("O número certo é:",num_secreto)