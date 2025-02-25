from forma_geométrica import Quadrado, Retangulo, Circulo

while True: #Cria um loop até digitar uma forma válida

    forma = input("Digite a forma geométrica (quadrado, retangulo ou circulo): ").strip().lower()

    if forma == "quadrado":
        lado = float(input("Digite o lado do quadrado: "))
        forma = Quadrado(lado)
        break #Sai do loop
    elif forma == "retangulo":
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        forma = Retangulo(base, altura)
        break
    elif forma == "circulo":
        raio = float(input("Digite o raio do círculo: "))
        forma = Circulo(raio)
        break
    else:
        print("Digite uma forma válida!")

print(f"A área do {forma} é: {forma.calcular_area():.2f}")