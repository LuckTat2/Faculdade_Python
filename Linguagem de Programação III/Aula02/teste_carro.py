from carro import Carro #Importação da classe


carro1 = Carro("Ford","Mustang","2000","Vermelho")
carro2 = Carro("Fiat","Uno","2010","Preto")

carro1.mostrar_detalhes()
carro2.mostrar_detalhes()

carro1.acelerar(50)
carro1.frear(20)
carro1.mostrar_detalhes()