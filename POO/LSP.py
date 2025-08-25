class Retangulo:
    def __init__(self):
        self.largura = 0
        self.altura = 0

    def set_largura(self, w: int):
        self.largura = w

    def set_altura(self, h: int):
        self.altura = h

    def area(self) -> int:
        return self.largura * self.altura


class Quadrado(Retangulo):
    def set_largura(self, w: int):
        self.largura = self.altura = w  

    def set_altura(self, h: int):
        self.largura = self.altura = h  


def testa_area_com_setters(r: Retangulo):
    r.set_largura(5)
    r.set_altura(4)
    
    print("Área esperada 20, obtida:", r.area())


print("Retângulo:")
testa_area_com_setters(Retangulo())  

print("Quadrado (substituindo Retângulo):")
testa_area_com_setters(Quadrado())   


## problema evitado
from abc import ABC, abstractmethod

class Forma2D(ABC):
    @abstractmethod
    def area(self) -> float: ...


class RetanguloOk(Forma2D):
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura


class QuadradoOk(Forma2D):
    def __init__(self, lado: float):
        self.lado = lado

    def area(self) -> float:
        return self.lado * self.lado


def imprime_area(f: Forma2D):
    print("Área:", f.area())


imprime_area(RetanguloOk(5, 4))  
imprime_area(QuadradoOk(4))      