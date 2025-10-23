from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @abstractmethod
    def descricao(self):
        pass

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.__autor = autor

    @property
    def autor(self):
        return self.__autor

    def descricao(self):
        print("Nome: {} - Preço: {} - Autor: {}".format(self.nome, self.preco, self.__autor))

class Eletronico(Produto):
    def __init__(self, nome, preco, garantia):
        super().__init__(nome, preco)
        self.__garantia = garantia

    @property
    def garantia(self):
        return self.__garantia
    
    def descricao(self):
        print("Nome: {} - Preço: {} - Garantia: {}".format(self.nome, self.preco, self.__garantia))

class Carrinho:
    def __init__(self):
        self.__itens = []

    @property
    def itens(self):
        return self.__itens
    
    def adicionar_item(self, produto):
        self.__itens.append(produto)
    
    def listar_itens(self):
        for item in self.__itens:
            print("Nome: {} - Preço: {}".format(item.nome, item.preco))

    def calcular_total(self):
        valor_total = 0
        for item in self.__itens:
            valor_total += item.preco
        return valor_total
    
if __name__ == "__main__":
    livro1 = Livro("Clean Code", 120.0, "Robert C. Martin")
    livro2 = Livro("Python Fluente", 150.0, "Luciano Ramalho")
    celular = Eletronico("Smartphone", 2500.0, 12)

    carrinho = Carrinho()
    carrinho.adicionar_item(livro1)
    carrinho.adicionar_item(livro2)
    carrinho.adicionar_item(celular)

    carrinho.listar_itens()
    print(f"Total do carrinho: R${carrinho.calcular_total()}")