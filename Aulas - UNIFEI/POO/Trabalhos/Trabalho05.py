#Matrícula:	2025015820

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = {}

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getPontoMensalFunc(self):
        return self.__pontoMensalFunc
    
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        self.__pontoMensalFunc[(mes, ano)] = PontoFunc(mes, ano, faltas, atrasos)

    def lancaFaltas(self, mes, ano, faltas):
        self.__pontoMensalFunc[(mes, ano)].lancaFaltas(faltas)

    def lancaAtrasos(self, mes, ano, atrasos):
        self.__pontoMensalFunc[(mes, ano)].lancaAtrasos(atrasos)

    def imprimeFolha(self, mes, ano):
        salarioLiquido = self.calculaSalario(mes, ano)
        bonus = self.calculaBonus(mes, ano)
        print("Código: {}".format(self.__codigo))
        print("Nome: {}".format(self.__nome))
        print("Salário líquido: {:.2f}".format(salarioLiquido))
        print("Bonus: {:.2f}".format(bonus))
    
    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass

class Professor(Funcionario):
    def __init__(self, codigo, nome, titulacao, salarioHora, nmrAulas):
        super().__init__(codigo, nome)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nmrAulas = nmrAulas

    def getTitulacao(self):
        return self.__titulacao
    
    def getSalarioHora(self):
        return self.__salarioHora
    
    def getNmrAulas(self):
        return self.__nmrAulas
    
    def calculaSalario(self, mes, ano):
        registro = self.getPontoMensalFunc().get((mes, ano))
        nmrFaltas = registro.getNmrFaltas()
        salarioTotal = self.__salarioHora * self.__nmrAulas - self.__salarioHora * nmrFaltas
        return salarioTotal
    
    def calculaBonus(self, mes, ano):
        registro = self.getPontoMensalFunc().get((mes, ano))
        nmrAtrasos = registro.getNmrAtrasos()
        percentualBonus = 10 - nmrAtrasos
        bonusTotal = self.calculaSalario(mes, ano) * (percentualBonus / 100)
        return bonusTotal

class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, funcao, salarioMensal):
        super().__init__(codigo, nome)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    def getFuncao(self):
        return self.__funcao
    
    def getSalarioMensal(self):
        return self.__salarioMensal
    
    def calculaSalario(self, mes, ano):
        registro = self.getPontoMensalFunc().get((mes, ano))
        nmrFaltas = registro.getNmrFaltas()
        salarioTotal = self.__salarioMensal - (self.__salarioMensal / 30) * nmrFaltas
        return salarioTotal

    def calculaBonus(self, mes, ano):
        registro = self.getPontoMensalFunc().get((mes, ano))
        nmrAtrasos = registro.getNmrAtrasos()
        percentualBonus = 8 - nmrAtrasos
        bonusTotal = self.calculaSalario(mes, ano) * (percentualBonus / 100)
        return bonusTotal
    
class PontoFunc:
    def __init__(self, mes, ano, nmrFaltas, nmrAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nmrFaltas = nmrFaltas
        self.__nmrAtrasos = nmrAtrasos

    def getMes(self):
        return self.__mes
    
    def getAno(self):
        return self.__ano
    
    def getNmrFaltas(self):
        return self.__nmrFaltas
    
    def getNmrAtrasos(self):
        return self.__nmrAtrasos
    
    def lancaFaltas(self, nmrFaltas):
        self.__nmrFaltas = nmrFaltas

    def lancaAtrasos(self, nmrAtrasos):
        self.__nmrAtrasos = nmrAtrasos

if __name__ == "__main__":
 funcionarios = []
 prof = Professor(1, "Joao", "Doutor", 45.35, 32)
 prof.adicionaPonto(4, 2021, 0, 0)
 prof.lancaFaltas(4, 2021, 2)
 prof.lancaAtrasos(4, 2021, 3)
 funcionarios.append(prof)
 tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
 tec.adicionaPonto(4, 2021, 0, 0)
 tec.lancaFaltas(4, 2021, 3)
 tec.lancaAtrasos(4, 2021, 4)
 funcionarios.append(tec)
 for func in funcionarios:
     func.imprimeFolha(4, 2021)
     print()