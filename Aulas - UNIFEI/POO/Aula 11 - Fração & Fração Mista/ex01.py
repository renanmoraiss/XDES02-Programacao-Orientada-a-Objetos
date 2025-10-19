#Exercício da Aula 11 - Fração Mista

class Fracao:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    @property
    def numerador(self):
        return self.__numerador
    
    @property
    def denominador(self):
        return self.__denominador
    
    def encontraMdc(self, numerador, denominador):
        while numerador % denominador != 0:
            oldnumerador = numerador
            olddenominador = denominador
            numerador = olddenominador
            denominador = oldnumerador % olddenominador
        return denominador
    
    def simplificaFracao(self):
        divisorComum = self.encontraMdc(self.__numerador, self.__denominador)
        self.__numerador = self.__numerador // divisorComum
        self.__denominador = self.__denominador // divisorComum

    def converteParaMista(self):
        inteiro = self.__numerador // self.__denominador
        numerador = self.__numerador % self.__denominador
        denominador = self.__denominador
        return FracaoMista(inteiro, numerador, denominador)
    
    def __add__(self, outraFracao):
        novoNumerador = self.__numerador * outraFracao.denominador + outraFracao.numerador * self.__denominador
        novoDenominador = self.__denominador * outraFracao.denominador
        divisorComum = self.encontraMdc(novoNumerador, novoDenominador)
        novoNumerador = novoNumerador // divisorComum
        novoDenominador = novoDenominador // divisorComum
        if (novoNumerador / novoDenominador) < 1:
            return Fracao(novoNumerador, novoDenominador)
        else:
            return Fracao(novoNumerador, novoDenominador).converteParaMista()
    
    def __str__(self):
        if (self.__numerador == self.__denominador):
            res = self.__numerador // self.__denominador
            return str(res)
        else:
            return str(self.__numerador) + "/" + str(self.__denominador)
    
class FracaoMista:
    def __init__(self, inteiro, numerador, denominador):
        self.__inteiro = inteiro
        self.__denominador = denominador
        self.__numerador = numerador
    
    @property
    def inteiro(self):
        return self.__inteiro
    
    @property
    def numerador(self):
        return self.__numerador
    
    @property
    def denominador(self):
        return self.__denominador
    
    def converteParaFracao(self):
        novoNumerador = ((self.__inteiro * self.__denominador) + self.__numerador)
        novoDenominador = self.__denominador
        return Fracao(novoNumerador, novoDenominador)
    
    def __add__(self, outraMista):
        return self.converteParaFracao() + outraMista.converteParaFracao()
    
    def __str__(self):
        if (self.__numerador == 0):
            res = self.__inteiro
            return str(res)
        else:
            return str(self.__inteiro) + ' ' + str(self.__numerador) + "/" + str(self.__denominador)
    
if __name__ == "__main__":
    fracao1 = Fracao(7,6)
    fracao2 = Fracao(13,7)
    print(fracao1 + fracao2)

    fracao3 = Fracao(1,3)
    fracao4 = Fracao(2,3)
    print(fracao3 + fracao4)

    fracaoMista2 = FracaoMista(3,1,2)
    fracaoMista3 = FracaoMista(4,2,3)
    print(fracaoMista2 + fracaoMista3)