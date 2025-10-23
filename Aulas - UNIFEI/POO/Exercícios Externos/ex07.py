from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome
    
    @property
    def salario(self):
        return self.__salario
    
    def exibir_info(self):
        pass
    
    @abstractmethod
    def calcular_pagamento(self):
        pass

class Medico(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.__pacientes = []

    def adicionar_paciente(self, nome):
        self.__pacientes.append(nome)

    def calcular_pagamento(self):
        totalPacientes = len(self.__pacientes)
        return (totalPacientes * 100) + self.salario
    
class Enfermeiro(Funcionario):
    def __init__(self, nome, salario, plantao):
        super().__init__(nome, salario)
        self._plantao = plantao

    @property
    def plantao(self):
        return self.__plantao
    
    def calcular_pagamento(self):
        return (self.__plantao * 200) + self.salario
    
class Hospital:
    def __init__(self, nome):
        self.__nome = nome
        self.__funcionarios = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def funcionarios(self):
        return self.__funcionarios
    
    def adicionar_funcionario(self, funcionario):
        self.__funcionarios.append(funcionario)

    def folha_pagamento(self):
        for func in self.__funcionarios:
            print("Nome: {} - Sal: {}".format(func.nome, func.salario))

if __name__ == "__main__":
    h = Hospital("Hospital São Lucas")

    m1 = Medico("Dr. Ana", 10000)
    m1.adicionar_paciente("Carlos")
    m1.adicionar_paciente("Maria")

    e1 = Enfermeiro("José", 4000, 5)

    h.adicionar_funcionario(m1)
    h.adicionar_funcionario(e1)

    h.folha_pagamento()