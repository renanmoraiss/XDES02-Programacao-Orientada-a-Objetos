from abc import ABC, abstractmethod
import math

class Forma(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.__largura = largura
        self.__altura = altura

    @property
    def largura(self):
        return self.__largura
    
    @property
    def altura(self):
        return self.__altura
    
    def area(self):
        return self.__largura * self.__altura
    
    def perimetro(self):
        return (2 * self.__largura) + (2 * self.__altura)

class Circulo(Forma):
    def __init__(self, raio):
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
    
    def area(self):
        return math.pi * (math.pow(self.__raio, 2))
    
    def perimetro(self):
        return 2 * math.pi * self.__raio

if __name__ == "__main__":
    formas = [
        Retangulo(4, 5),
        Circulo(3),
        Retangulo(10, 2),
    ]

    for f in formas:
        print(f"{type(f).__name__}:")
        print(f"  Área: {f.area()}")
        print(f"  Perímetro: {f.perimetro()}")
        print("-" * 25)