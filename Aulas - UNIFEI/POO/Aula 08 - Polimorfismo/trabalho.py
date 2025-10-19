#Trabalho da Aula 08 - (04) Polimorfismo

from abc import ABC, abstractmethod
class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @abstractmethod
    def salario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @property
    def valorPorHora(self):
        return self.__valorPorHora
    
    def salario(self):
        return self.__horasTrabalhadas * self.__valorPorHora
    
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados
    
    @property
    def valorPorDia(self):
        return self.__valorPorDia
    
    def salario(self):
        return self.__diasTrabalhados * self.__valorPorDia
    
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal
    
    @property
    def valorMensal(self):
        return self.__valorMensal
    
    def salario(self):
        return self.__valorMensal
    
if __name__ == "__main__":
    horista = Horista("Carla", "359916235", 160, 12)
    diarista = Diarista("Andreia", "359124958", 20, 65)
    mensalista = Mensalista("Dandara", "359259359", 1200)
    empregadas = [horista, diarista, mensalista]

    for i in empregadas:
        print("{}, {}".format(i.nome, i.salario()))
    print()

    opcaoMaisBarata = empregadas[0].salario()
    index = i
    for i in range(0,3):
        if (empregadas[i].salario() < opcaoMaisBarata):
            index = i

    print("Opção mais barata:")
    print("Nome: {}".format(empregadas[index].nome))
    print("Telefone: {}".format(empregadas[index].telefone))
    print("Salário: {}".format(empregadas[index].salario()))