from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, valor):
        self.__telefone = valor
    
    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

    def getSalario(self):
        salarioTotal = self.__horasTrabalhadas * self.__valorPorHora
        return salarioTotal
            
class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    def getSalario(self):
        salarioTotal = self.__diasTrabalhados * self.__valorPorDia
        return salarioTotal
            
class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    def getSalario(self):
        return self.__valorMensal

if __name__ == "__main__":
    horista = Horista("Alicia", "99185-3354", 160, 12)
    diarista = Diarista("Julia", "99124-1239", 20, 65)
    mensalista = Mensalista("Alice", "99120-3421", 1200)
    print("Salário da Horista: R${:.2f}".format(horista.getSalario()))
    print("Salário da Diarista: R${:.2f}".format(diarista.getSalario()))
    print("Salário da Mensalista: R${:.2f}".format(mensalista.getSalario()))
    empregadas = [horista, diarista, mensalista]
    empregadaMaisBarata = empregadas[0]
    for salario in empregadas:
        if salario.getSalario() < empregadaMaisBarata.getSalario():
            empregadaMaisBarata = salario
    print("Opção mais barata: {}, {}, R${:.2f}".format(empregadaMaisBarata.nome, empregadaMaisBarata.telefone, empregadaMaisBarata.getSalario()))