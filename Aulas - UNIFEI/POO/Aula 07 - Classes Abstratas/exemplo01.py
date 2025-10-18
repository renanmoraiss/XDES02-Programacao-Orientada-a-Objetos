#Exemplo para usar a biblioteca 'abc'

from abc import ABC, abstractmethod

#criando uma classe abstrata
class MinhaClasse(ABC):
    #definindo um método abstrato
    @abstractmethod 
    def meuMetodo(self):
        pass