class TitulacaoInvalida(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class IdadeMenorQuePermitida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class CpfDuplicado(Exception):
    pass

class Pessoa:
    def __init__(self, nome, cpf, endereco, idade):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    def printDescricao(self):
        print("Nome: {}".format(self.__nome))
        print("CPF: {}".format(self.__cpf))
        print("Endereço: {}".format(self.__endereco))
        print("Idade: {}".format(self.__idade))

class Professor(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, titulacao):
        super().__init__(nome, cpf, endereco, idade)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        super().printDescricao()
        print("Titulação: {}".format(self.__titulacao))

class Aluno(Pessoa):
    def __init__(self, nome, cpf, endereco, idade, curso):
        super().__init__(nome, cpf, endereco, idade)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        super().printDescricao()
        print("Curso: {}".format(self.__curso))

if __name__ == "__main__":
    pessoas_cadastradas = []
    cpfs_cadastrados = []
    lista_dados = [
        Aluno("Renan", "122", "Rua dos Estudantes", 18, "SIN"),
        Aluno("Alicia", "123", "Rua dos Estudantes", 17, "CCO"),
        Aluno("Tiago", "125", "Rua dos Estudantes", 17, "ECO"),
        Aluno("Bianca", "126", "Rua dos Estudantes", 19, "SIN"),
        Professor("Rodrigo", "127", "Rua dos Docentes", 29, "doutor"),
        Professor("Roberto", "128", "Rua dos Docentes", 30, "Mestre"),
        Professor("Alice", "129", "Rua dos Docentes", 29, "Mestre"),
        Professor("Mirian", "126", "Rua dos Docentes", 32, "doutor")
    ]
    for pessoa in lista_dados:
        try:
            if pessoa.cpf in cpfs_cadastrados:
                raise CpfDuplicado
            if isinstance(pessoa, Professor):
                if (pessoa.titulacao.lower() != "doutor"):
                    raise TitulacaoInvalida
                if (pessoa.idade < 30):
                    raise IdadeInvalida
            if isinstance(pessoa, Aluno):
                if ((pessoa.curso.upper() != "SIN") and (pessoa.curso.upper() != "CCO")):
                    raise CursoInvalido
                if (pessoa.idade < 18):
                    raise IdadeMenorQuePermitida
            pessoas_cadastradas.append(pessoa)
            cpfs_cadastrados.append(pessoa.cpf)
            print("{} cadastrado com sucesso".format(pessoa.nome))
        except:
            print("Erro ao cadastrar {}".format(pessoa.nome))
    
    print("Usuários Cadastrados:")
    for pessoa in pessoas_cadastradas:
        pessoa.printDescricao()