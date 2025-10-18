#Exercício da Aula 07

from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, marca, modelo, cor, docto):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__docto = docto

    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def cor(self):
        return self.__cor

    @property
    def docto(self):
        return self.__docto
    
    @abstractmethod
    def printDados(self):
        pass

    def printDadosVeiculo(self):
        print("{}, {}, {}".format(self.__docto.placa, self.__docto.renavam, self.__docto.ipva))

class Documento:
    def __init__(self, placa, renavam, ipva):
        self.__placa = placa
        self.__renavam = renavam
        self.__ipva = ipva
    
    @property
    def placa(self):
        return self.__placa
    
    @property
    def renavam(self):
        return self.__renavam
    
    @property
    def ipva(self):
        return self.__ipva

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, docto, tipo):
        super().__init__(marca, modelo, cor, docto)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo
    
    def printDados(self):
        print("{}, {}, {}, {}".format(self.marca, self.modelo, self.cor, self.__tipo))
        print("Docto:")
        super().printDadosVeiculo()

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, docto, estilo):
        super().__init__(marca, modelo, cor, docto)
        self.__estilo = estilo

    @property
    def estilo(self):
        return self.__estilo
    
    def printDados(self):
        print("{}, {}, {}, {}".format(self.marca, self.modelo, self.cor, self.__estilo))
        print("Docto:")
        super().printDadosVeiculo()

if __name__ == "__main__":
    documento1 = Documento("T34FK", "242354598", "2500")
    carro = Carro("Hyunday", "Creta", "Preto", documento1, "Toyota")
    carro.printDados()
    print()
    documento2 = Documento("TE35K", "35235092", "1600")
    moto = Moto("Yamaha", "MT-03", "Preta", documento2, "Naked")
    moto.printDados()