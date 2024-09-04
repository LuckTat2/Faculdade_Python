
totalVista = 0
prazo = 0

for i in range(5):
    cod = input("Compra à vista ou à prazo? Digite v ou p: ")
    preco = float(input("Digite o preço do produto: "))
    if cod == "v":
        totalVista = totalVista + preco
    else:
        prazo = prazo + preco

porcentagemPrazo = prazo * 0.1

totalPrazo = prazo + porcentagemPrazo

totalCompras = totalVista + totalPrazo

print("O total das vendas à vista é: R${:.2f}, das vendas à prazo é: R${:.2f} e a soma total é: R${:.2f}".format(totalVista, totalPrazo, totalCompras))