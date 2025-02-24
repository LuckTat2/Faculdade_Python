idade = 0
peso = 0
altura = 0
idade_maior = 0
total_altura = 0
qt_altura = 0
peso_inferior = 0

for i in range(15):
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    altura = float(input("Digite a altura da pessoa: "))

    if idade > 50:
        idade_maior += 1
    if idade >= 20 and idade <= 30:
        total_altura = total_altura + altura
        qt_altura += 1
    if peso < 60:
        peso_inferior += 1

if qt_altura > 0:
    media_altura = total_altura / qt_altura
else:
    media_altura = 0

p_peso = (peso_inferior / 15) * 100

print("O total de pessoas com idade superior a 50 anos é:",idade_maior)
print("A média de alturas entre 20 e 30 anos é:",media_altura)
print("A percentagem das pessoas com peso inferior a 60kg é: {:.2f}".format(p_peso))