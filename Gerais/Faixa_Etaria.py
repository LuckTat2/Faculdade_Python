faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0
idade = 0

for i in range(15):
    idade = int(input("Digite a idade da pessoa: "))
    
    if idade < 0 and idade > 105:
        print("Digite uma idade válida!")
    elif idade <= 15:
        faixa1 += 1
    elif idade >= 16 and idade <= 30:
        faixa2 += 1
    elif idade >= 31 and idade <= 45:
        faixa3 += 1
    elif idade >= 46 and idade <= 60:
        faixa4 += 1
    else:
        faixa5 += 1

p_faixa1 = (faixa1 / 15) * 100
p_faixa5 = (faixa5 / 15) * 100

print("O total de pessoas entre 0 e 15 anos é:",faixa1)
print("O total de pessoas entre 16 e 30 anos é:",faixa2)
print("O total de pessoas entre 31 e 45 anos é:",faixa3)
print("O total de pessoas entre 46 e 60 anos é:",faixa4)
print("O total de pessoas com 61 anos ou acima é:",faixa5)
print("A percentagem de pessoas na faixa 1 é de: {:.2f}%".format(p_faixa1))
print("A percentagem de pessoas na faixa 5 é de: {:.2f}%".format(p_faixa5))