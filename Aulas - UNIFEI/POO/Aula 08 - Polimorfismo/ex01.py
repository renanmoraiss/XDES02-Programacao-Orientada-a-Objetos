#Exercício da Aula 08

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
    
    def calculaImposto(self, salarioBruto):
        if salarioBruto >= 1903.9:
            if salarioBruto < 2826.65:
                imposto = 7.5
            elif salarioBruto < 3751.05:
                imposto = 15
            elif salarioBruto < 4664.68:
                imposto = 22.5
            else:
                imposto = 27.5
        else:
            imposto = 0
        return (salarioBruto * imposto) / 100
    
    @abstractmethod
    def calculaSalario(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioBruto):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioBruto

    @property
    def salarioBruto(self):
        return self.__salarioBruto
    
    @salarioBruto.setter
    def salarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto        
    
    def calculaSalario(self):
        previdencia = self.__salarioBruto * 0.11
        imposto = self.calculaImposto(self.__salarioBruto)
        return self.__salarioBruto - imposto - previdencia
    
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
        imposto = self.calculaImposto(self.cargaHoraria * self.__salarioHora)
        return ((self.cargaHoraria * self.__salarioHora) - imposto)

    
if __name__ == "__main__":
    profDe = ProfDE("Alberto", 333, 40, 1200)
    profHorista = ProfHorista("José", 444, 50, 80)
    profDe.salario = 1500
    profHorista.salarioHora = 85
    profs = [profDe, profHorista]
    for prof in profs:
        print("{}, {}".format(prof.nome, prof.calculaSalario()))