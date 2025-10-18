#Sistema Academico - Parte 01

from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, endereco, idade):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao):
        super().__init__(nome, endereco, idade)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print("{}, {}, {}, {}".format(self.nome, self.endereco, self.idade, self.__titulacao))

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso):
        super().__init__(nome, endereco, idade)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        print("{}, {}, {}, {}".format(self.nome, self.endereco, self.idade, self.__curso))

if __name__ == "__main__":
    prof = Professor("Alberto", "Rua do Professor", 43, "Mestrado em Física")
    prof.printDescricao()
    aluno = Aluno("Renan", "Rua do Aluno", 19, "SIN")
    aluno.printDescricao()