#Trabalho da Aula 07 - Classes e Métodos Abstratos

from abc import ABC, abstractmethod
import math
class FormaGeo(ABC):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def printDados(self):
        pass

class Retangulo(FormaGeo):
    def __init__(self, nome, altura, largura):
        super().__init__(nome)
        self.__altura = altura
        self.__largura = largura

    @property
    def altura(self):
        return self.__altura
    
    @property
    def largura(self):
        return self.__largura
    
    def area(self):
        return (self.__altura * self.__largura)
    
    def perimetro(self):
        return (self.__altura + self.__altura) + (self.__largura + self.__largura)
    
    def printDados(self):
        print("Nome: {}".format(self.nome))
        print("Area: {:.2f}".format(self.area()))
        print("Perimetro: {:.2f}".format(self.perimetro()))

class Circulo(FormaGeo):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
    
    def area(self):
        return (math.pi * (self.__raio * self.__raio))
    
    def perimetro(self):
        return (2 * math.pi * self.__raio)
    
    def printDados(self):
        print("Nome: {}".format(self.nome))
        print("Area: {:.2f}".format(self.area()))
        print("Perimetro: {:.2f}".format(self.perimetro()))

class HexagonoRegular(FormaGeo):
    def __init__(self, nome, lado):
        super().__init__(nome)
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado
    
    def area(self):
        return (3 * math.sqrt(3) * (self.__lado * self.__lado) / 2)
    
    def perimetro(self):
        return (6 * self.__lado)
    
    def printDados(self):
        print("Nome: {}".format(self.nome))
        print("Area: {:.2f}".format(self.area()))
        print("Perimetro: {:.2f}".format(self.perimetro()))

if __name__ == "__main__":
    retangulo = Retangulo("Retangulo", 10, 15)
    retangulo.printDados()
    circulo = Circulo("Circulo", 10)
    circulo.printDados()
    hexRegular = HexagonoRegular("Hexagono Regular", 10)
    hexRegular.printDados()