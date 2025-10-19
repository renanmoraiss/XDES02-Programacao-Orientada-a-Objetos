from abc import ABC, abstractmethod
class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def cargaHoraria(self):
        return self.__cargaHoraria
    
    @abstractmethod
    def calculaSalario(self):
        pass

    @abstractmethod
    def printDados(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salario):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    
    def calculaSalario(self):
        return self.__salario
    
    def printDados(self):
        print("{}, {}".format(self.nome, self.__salario))
    
class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora
    
    def calculaSalario(self):
        return self.__salarioHora * self.cargaHoraria
    
    def printDados(self):
        print("{}, {}".format(self.nome, self.calculaSalario()))
    
if __name__ == "__main__":
    profDe = ProfDE("Alberto", 333, 40, 1200)
    profHorista = ProfHorista("José", 444, 50, 80)
    print("Antes do setter:")
    profDe.printDados()
    profHorista.printDados()
    print()
    profDe.salario = 1500
    profHorista.salarioHora = 85
    profs = [profDe, profHorista]
    print("Depois do setter:")
    for prof in profs:
        print("{}, {}".format(prof.nome, prof.calculaSalario()))