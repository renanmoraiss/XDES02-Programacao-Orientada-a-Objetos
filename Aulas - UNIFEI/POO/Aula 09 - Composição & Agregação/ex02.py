#Exercício da Aula 09

from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @abstractmethod
    def descrever(self):
        pass

class Instrutor(Pessoa):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.__especialidade = especialidade

    @property
    def especialidade(self):
        return self.__especialidade
    
    def descrever(self):
        print("{}, {}, {}".format(self.nome, self.email, self.__especialidade))

class Aluno(Pessoa):
    def __init__(self, nome, email, matricula):
        super().__init__(nome, email)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula
    
    def descrever(self):
        print("{}, {}, {}".format(self.nome, self.email, self.__matricula))

class Curso:
    def __init__(self, titulo, instrutor):
        self.__titulo = titulo
        self.__instrutor = instrutor
        self.__listaAlunos = []
        self.__listaAulas = []

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def instrutor(self):
        return self.__instrutor
    
    @property
    def listaAlunos(self):
        return self.__listaAlunos
    
    @property
    def listaAulas(self):
        return self.__listaAulas
    
    def adicionarAluno(self, aluno):
        self.__listaAlunos.append(aluno)

    def adicionarAula(self, aula):
        self.__listaAulas.append(aula)

    def exibirDetalhes(self):
        print("Curso: {}".format(self.__titulo))
        print("Instrutor: {} (Especialidade: {})".format(self.instrutor.nome, self.instrutor.especialidade))
        print()
        print("Alunos:")
        for aluno in self.__listaAlunos:
            print("- {} (Matrícula: {})".format(aluno.nome, aluno.matricula))
        print()
        print("Aulas:")
        for aula in self.__listaAulas:
            print("- {} ({} min)".format(aula.titulo, aula.duracao))

class Aula:
    def __init__(self, titulo, duracao):
        self.__titulo = titulo
        self.__duracao = duracao

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def duracao(self):
        return self.__duracao
    
    def exibirAula(self):
        print("{}, {}".format(self.__titulo, self.__duracao))

if __name__ == "__main__":
    instrutor1 = Instrutor("Carlos", "carlos@curso.com", "Backend")

    aluno1 = Aluno("Renan", "renan@email.com", 1023)
    aluno2 = Aluno("Maria", "maria@email.com", 1045)
    aluno3 = Aluno("João", "joao@email.com", 1060)

    curso_python = Curso("Programação em Python", instrutor1)

    curso_python.adicionarAluno(aluno1)
    curso_python.adicionarAluno(aluno2)
    curso_python.adicionarAluno(aluno3)

    curso_python.adicionarAula(Aula("Introdução à Linguagem", 30))
    curso_python.adicionarAula(Aula("Estruturas de Controle", 45))
    curso_python.adicionarAula(Aula("Orientação a Objetos", 60))

    curso_python.exibirDetalhes()