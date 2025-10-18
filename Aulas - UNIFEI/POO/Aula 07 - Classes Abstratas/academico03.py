#Sistema Academico - Parte 03

from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, endereco, idade):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__listaDisc = []
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def listaDisc(self):
        return self.__listaDisc
    
    def insereDisc(self, disc):
        self.__listaDisc.append(disc)
    
    @abstractmethod
    def printDescricao(self):
        pass

class Disciplina:
    def __init__(self, nomeDisc, cargaHoraria):
        self.__nomeDisc = nomeDisc
        self.__cargaHoraria = cargaHoraria

    @property
    def nomeDisc(self):
        return self.__nomeDisc
    
    @property
    def cargaHoraria(self):
        return self.__cargaHoraria

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao):
        super().__init__(nome, endereco, idade)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print("{}, {}, {}, {}".format(self.nome, self.endereco, self.idade, self.__titulacao))
        for disciplina in self.listaDisc:
            print("{}, {}".format(disciplina.nomeDisc, disciplina.cargaHoraria))

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso):
        super().__init__(nome, endereco, idade)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        print("{}, {}, {}, {}".format(self.nome, self.endereco, self.idade, self.__curso))
        for disciplina in self.listaDisc:
            print("{}, {}".format(disciplina.nomeDisc, disciplina.cargaHoraria))

if __name__ == "__main__":
    disciplina1 = Disciplina("Física", 64)
    disciplina2 = Disciplina("Cálculo A", 64)
    disciplina3 = Disciplina("Banco de Dados I", 64)

    prof = Professor("Alberto", "Rua do Professor", 43, "Mestrado em Física")
    prof.insereDisc(disciplina1)
    prof.insereDisc(disciplina2)
    prof.printDescricao()
    aluno = Aluno("Renan", "Rua do Aluno", 19, "SIN")
    aluno.insereDisc(disciplina3)
    aluno.printDescricao()