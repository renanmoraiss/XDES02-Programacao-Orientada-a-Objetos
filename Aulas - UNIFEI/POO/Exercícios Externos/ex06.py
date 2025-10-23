from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @abstractmethod
    def exibir_info(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, departamento):
        super().__init__(nome, idade)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento
    
    def exibir_info(self):
        print("Nome: {} - Idade: {} - Depart: {}".format(self.nome, self.idade, self.__departamento))
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula
    
    def exibir_info(self):
        print("Nome: {} - Idade: {} - Matric: {}".format(self.nome, self.idade, self.__matricula))

class Disciplina:
    def __init__(self, nome, professor):
        self.__nome = nome
        self.__professor = professor
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def professor(self):
        return self.__professor
    
    @property
    def alunos(self):
        return self.__alunos
    
    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def listar_participantes(self):
        for participante in self.__alunos:
            print("Nome: {} - Idade: {} - Matric: {}".format(participante.nome, participante.idade, participante.matricula))

if __name__ == "__main__":
    prof = Professor("Dr. João", 45, "Computação")
    a1 = Aluno("Renan", 21, "202301")
    a2 = Aluno("Lívia", 20, "202302")

    poo = Disciplina("Programação Orientada a Objetos", prof)
    poo.adicionar_aluno(a1)
    poo.adicionar_aluno(a2)

    poo.listar_participantes()