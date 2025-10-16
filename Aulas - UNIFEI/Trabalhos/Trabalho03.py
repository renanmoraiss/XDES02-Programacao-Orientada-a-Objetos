#Matrícula:	2025015820

from abc import ABC, abstractmethod
import math

class formaGeo(ABC):

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
    
class Retangulo(formaGeo):
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
        return self.__altura*self.__largura
    
    def perimetro(self):
        return 2*(self.__altura + self.__largura)
        
    def printDados(self):
        print('Nome: {}'.format(self.nome))
        print('Área: {:.2f}'.format(self.area()))
        print('Perimetro: {:.2f}'.format(self.perimetro()))

class Circulo(formaGeo):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
    
    def area(self):
        return math.pi*(self.__raio**2)
    
    def perimetro(self):
        return 2*math.pi*self.__raio
    
    def printDados(self):
        print('Nome: {}'.format(self.nome))
        print('Área: {:.2f}'.format(self.area()))
        print('Perimetro: {:.2f}'.format(self.perimetro()))

class HexagonoRegular(formaGeo):
    def __init__(self, nome, lado):
        super().__init__(nome)
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado
    
    def area(self):
        return 6*((self.__lado**2)*math.sqrt(3) / 4)
    
    def perimetro(self):
        return 6*self.__lado
    
    def printDados(self):
        print('Nome: {}'.format(self.nome))
        print('Área: {:.2f}'.format(self.area()))
        print('Perimetro: {:.2f}'.format(self.perimetro()))

if __name__ == "__main__":
    ret = Retangulo('Retângulo', 20, 10)
    ret.printDados()
    circ = Circulo('Círculo', 10)
    circ.printDados()
    hex = HexagonoRegular('Hexágono Regular', 10)
    hex.printDados()