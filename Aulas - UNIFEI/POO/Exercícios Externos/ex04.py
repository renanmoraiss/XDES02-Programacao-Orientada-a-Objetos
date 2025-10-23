class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    def exibir_info(self):
        print("{} - {}".format(self.__nome, self.__matricula))

class Escola:
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def alunos(self):
        return self.__alunos
    
    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)

    def listar_alunos(self):
        for aluno in self.__alunos:
            print ("Nome: {} - Matrícula: {}".format(aluno.nome, aluno.matricula))
        
if __name__ == "__main__":
    escola = Escola("Colégio Python")

    a1 = Aluno("Lucas", "A001")
    a2 = Aluno("Mariana", "A002")
    a3 = Aluno("Rafael", "A003")

    escola.adicionar_aluno(a1)
    escola.adicionar_aluno(a2)
    escola.adicionar_aluno(a3)

    print(f"Alunos da escola {escola.nome}:")
    escola.listar_alunos()