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

class Funcionario(Pessoa):
    def __init__(self, nome, email, cargo):
        super().__init__(nome, email)
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo
    
    def descrever(self):
        print("{}, {}, {}".format(self.nome, self.email, self.__cargo))

class Gerente(Pessoa):
    def __init__(self, nome, email, setor):
        super().__init__(nome, email)
        self.__setor = setor
    
    @property
    def setor(self):
        return self.__setor
    
    def descrever(self):
        print("{}, {}, {}".format(self.nome, self.email, self.__setor))

class Projeto:
    def __init__(self, nome, gerente):
        self.__nome = nome
        self.__gerente = gerente
        self.__listaTarefas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def gerente(self):
        return self.__gerente
    
    @property
    def listaTarefas(self):
        return self.__listaTarefas
    
    def adicionarTarefa(self, tarefa):
        self.__listaTarefas.append(tarefa)

    def descrever(self):
        print("Projeto: {}".format(self.nome))
        print("Gerente: {} (Setor: {})".format(self.gerente.nome, self.gerente.setor))
        print("Tarefas:")
        for tarefa in self.__listaTarefas:
            print("- {}, (Responsável: {}, Duração: {} dias)".format(tarefa.titulo, tarefa.responsavel.nome, tarefa.duracao))


class Tarefa:
    def __init__(self, titulo, responsavel, duracao):
        self.__titulo = titulo
        self.__responsavel = responsavel
        self.__duracao = duracao
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def responsavel(self):
        return self.__responsavel
    
    @property
    def duracao(self):
        return self.__duracao
    
    def descrever(self):
        print("{}, {}, {}".format(self.__titulo, self.__responsavel, self.__duracao))

if __name__ == "__main__":
    g1 = Gerente("Ana", "ana@empresa.com", "Tecnologia")
    f1 = Funcionario("Renan", "renan@empresa.com", "Desenvolvedor")
    f2 = Funcionario("Bruno", "bruno@empresa.com", "Designer")

    p1 = Projeto("App Mindly", g1)

    p1.adicionarTarefa(Tarefa("Criar Protótipo", f2, 5))
    p1.adicionarTarefa(Tarefa("Programar Backend", f1, 10))

    p1.descrever()