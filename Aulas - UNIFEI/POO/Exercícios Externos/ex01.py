class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, valor):
        self.__salario = valor

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.__setor = setor

    @property
    def setor(self):
        return self.__setor
    
    def exibir_dados(self):
        return ("Nome: {} - Salário {} - Setor: {}".format(self.nome, self.salario, self.__setor))
    
if __name__ == "__main__":
    f1 = Funcionario("Carlos", 3000.0)
    g1 = Gerente("Mariana", 7000.0, "TI")

    print(f"Funcionário: {f1.nome} - Salário: R${f1.salario:.2f}")
    print(f"Gerente: {g1.nome} - Salário: R${g1.salario:.2f} - Setor: {g1.setor}")