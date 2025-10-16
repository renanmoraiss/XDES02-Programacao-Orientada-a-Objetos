from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    @property
    def salario(self):
        return self.__salario
    
    @property
    def matricula(self):
        return self.__matricula
    
    @property
    def cargaHoraria(self):
        return self.__cargaHoraria
    
    def calcularImpostoRenda(self, salarioBruto):
        if (self.__salarioBruto < 1903.98):
            imposto = 0
        else:
            if (self.salarioBruto <= 2826.65):
                imposto = 7.5
            elif (self.__salarioBruto <= 3751.05):
                imposto = 15
            elif (self.__salarioBruto <= 4664.48):
                imposto = 22.5
            else:
                imposto = 27.5
        return ((self.__salarioBruto * imposto) / 100)

    @abstractmethod
    def calcularSalario(self):
        pass

class ProfessorHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @salarioHora.setter
    def salarioHora(self, salarioHora):
        self.__salarioHora = salarioHora

    def calcularSalario(self):
        salarioBruto = self.__salarioHora * self.__cargaHoraria
        previd = (salarioBruto * 0.11)
        imposto = self.calcularImpostoRenda(salarioBruto)
        salarioLiquido = self.__salarioBruto (previd + imposto)
        return salarioLiquido
       
class ProfessorDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioBruto):
        super().__init(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioBruto

    @property
    def salarioBruto(self):
        return self.__salarioBruto
    
    @salarioBruto.setter
    def salarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def calcularSalario(self):
        previd = (self._salarioBruto * 0.11)
        imposto = self.calcularImpostoRenda(self.__salarioBruto)
        salarioLiquido = self.__salarioBruto - (previd + imposto)
        return salarioLiquido

if __name__ == "__name__":
    prof1 = ProfessorDE('Renan', 12345, 60, 1500)
    prof2 = ProfessorHorista('Ronan', 12345, 60, 1500)
    prof1.salarioBruto = 6000
    prof2.salarioHora = 500
    profs = [prof1, prof2]
    for prof in profs:
        print('Nome: {} - Salario Bruto - {:.2f} - SalarioLiquido - {:.2f}'.format(prof.nome, prof.salario(), prof.calcularSalario()))