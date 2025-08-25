from abc import ABC, abstractmethod
import math

# Abstração: novas formas só precisam implementar "area"
class Forma(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Retangulo(Forma):
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura


class Circulo(Forma):
    def __init__(self, raio: float):
        self.raio = raio

    def area(self) -> float:
        return math.pi * (self.raio ** 2)


# A calculadora NÃO precisa saber que forma é.
class CalculadoraArea:
    @staticmethod
    def calcular(forma: Forma) -> float:
        return forma.area()


# uso
formas = [Retangulo(3, 4), Circulo(2)]
for f in formas:
    print("Área:", CalculadoraArea.calcular(f))
