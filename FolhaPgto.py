horasTrabalhadas = int(input("Digite suas horas trabalhadas: "))
valorHora = float(input("Digite o valor da sua hora: "))

salarioBruto = horasTrabalhadas * valorHora

sindicato = salarioBruto * 0.03
fgts = salarioBruto * 0.11
salarioLiquido = salarioBruto - sindicato
ir = 0.0
inss = 0.0

if salarioBruto >= 2259.21 and salarioBruto <= 2826.65:
    ir = salarioBruto * 0.075
    salarioLiquido = salarioLiquido - ir
elif salarioBruto >= 2826.66 and salarioBruto <= 3751.05:
    ir = salarioBruto * 0.15
    salarioLiquido = salarioLiquido - ir
elif salarioBruto >= 3751.06 and salarioBruto <= 4664.68:
    ir = salarioBruto * 0.225
    salarioLiquido = salarioLiquido - ir
elif salarioBruto > 4664.68:
    ir = salarioBruto * 0.275
    salarioLiquido = salarioLiquido - ir

if salarioBruto <= 1412.00:
    inss = salarioBruto * 0.075
    salarioLiquido = salarioLiquido - inss
elif salarioBruto >= 1412.01 and salarioBruto <= 2666.68:
    inss = salarioBruto * 0.09 - 21.18
    salarioLiquido = salarioLiquido - inss
elif salarioBruto >= 2666.69 and salarioBruto <= 4000.03:
    inss = salarioBruto * 0.12 - 101.18
    salarioLiquido = salarioLiquido - inss
elif salarioBruto >= 4000.04 and salarioBruto <= 7786.02:
    inss = salarioBruto * 0.14 - 181.18
    salarioLiquido = salarioLiquido - inss

print("Salario Bruto: {:.2f}".format(salarioBruto))
print("Desconto sindicato: {:.2f}".format(sindicato))
print("Desconto IR: {:.2f}".format(ir))
print("Desconto INSS: {:.2f}".format(inss))
print("Valor FGTS: {:.2f}".format(fgts))
print("Salário Líquido: {:.2f}".format(salarioLiquido))