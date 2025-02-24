def mostrar_menu():
    print("Menu de Pizzas:")
    print("Código | Descrição    | Pizza Média (R$) | Pizza Grande (R$)")
    print("------------------------------------------------------------")
    print("  21   | Napolitana   |       40,00      |       60,00")
    print("  22   | Margherita   |       35,00      |       55,00")
    print("  23   | Calabresa    |       45,00      |       65,00")
    print("  24   | Portuguesa   |       60,00      |       80,00")
    print("  25   | Frango       |       50,00      |       70,00")
    print("------------------------------------------------------------")


def calcular_total(qtd_pizzas, pizzas, modo_entrega):
    taxa_entrega = 10.00 if modo_entrega == 'entrega' else 0.00
    total = sum(pizza['preco'] for pizza in pizzas) + taxa_entrega
    return total


def main():
    mostrar_menu()
    
    qtd_pizzas = int(input("Informe a quantidade de pizzas: "))
    
    pizzas = []
    
    for i in range(qtd_pizzas):
        tamanho = input("Informe o tamanho da pizza (M/G): ").upper()
        codigo = int(input("Informe o código da pizza: "))
        
        # Preço baseado no tamanho
        if tamanho == 'M':
            if codigo == 21:
                preco = 40.00
            elif codigo == 22:
                preco = 35.00
            elif codigo == 23:
                preco = 45.00
            elif codigo == 24:
                preco = 60.00
            elif codigo == 25:
                preco = 50.00
            else:
                print("Código inválido!")
                continue
        elif tamanho == 'G':
            if codigo == 21:
                preco = 60.00
            elif codigo == 22:
                preco = 55.00
            elif codigo == 23:
                preco = 65.00
            elif codigo == 24:
                preco = 80.00
            elif codigo == 25:
                preco = 70.00
            else:
                print("Código inválido!")
                continue
        else:
            print("Tamanho inválido! Informe M ou G.")
            continue
        
        pizzas.append({'codigo': codigo, 'tamanho': tamanho, 'preco': preco})

    modo_entrega = input("Será entrega ou balcão? (entrega/balcão): ").lower()
    
    if modo_entrega not in ['entrega', 'balcão']:
        print("Modo de entrega inválido! O programa será encerrado.")
        return

    total = calcular_total(qtd_pizzas, pizzas, modo_entrega)

    print(f"\nTotal a pagar: R$ {total:.2f}")