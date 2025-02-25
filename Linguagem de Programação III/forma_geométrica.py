import math

class FormaGeometrica:
    def calcular_area(self):
        pass #Método abstrato

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def __str__(self):
        return "quadrado"
    
class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def __str__(self):
        return "retângulo"
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def __str__(self):
        return "círculo"