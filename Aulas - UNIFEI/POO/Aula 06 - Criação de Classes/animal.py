#Exemplo de Herança

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    #getter
    def getNome(self):
        return self.__nome
    
    @property
    def nome(self):
        return self.__nome
    
    #método
    def fazerCarinho(self):
        print("{} está recebendo carinho".format(self.__nome))

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome) #nome é herdado da superclasse Animal, por issa usa o super()
        self.__raca = raca

    @property
    def raca(self):
        return self.__raca
    
    #método
    def miar(self):
        print("meow meow")

class Cao(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.__raca = raca
    
    @property
    def raca(self):
        return self.__raca
    
    #método
    def latir(self):
        print("au au")

if __name__ == "__main__":
    gato = Gato("Thor", "Siames")
    print(gato.nome)
    print(gato.raca)
    gato.miar()
    gato.fazerCarinho()
    cao = Cao("Trovao", "Bulldog")
    print(cao.getNome())
    print(cao.raca)
    cao.latir()
    cao.fazerCarinho()
