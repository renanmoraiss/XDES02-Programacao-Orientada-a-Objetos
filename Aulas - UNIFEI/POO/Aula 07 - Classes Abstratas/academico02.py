#Sistema Academico - Parte 02

from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, listaDisc):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__listaDisc = listaDisc
    
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
    def __init__(self, nome, endereco, idade, titulacao, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print("{}, {}, {}, {}".format(self.nome, self.endereco, self.idade, self.__titulacao))
        for disciplina in self.listaDisc:
            print("{}, {}".format(disciplina.nomeDisc, disciplina.cargaHoraria))

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
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

    listaDisc = [disciplina1, disciplina2, disciplina3]

    prof = Professor("Alberto", "Rua do Professor", 43, "Mestrado em Física", listaDisc)
    prof.printDescricao()
    aluno = Aluno("Renan", "Rua do Aluno", 19, "SIN", listaDisc)
    aluno.printDescricao()