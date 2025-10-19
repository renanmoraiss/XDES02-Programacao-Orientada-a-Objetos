#Exemplo de Fração

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
    
    def encontraMdc(self, m, n):
        while m%n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm%oldn
        return n
    
    def simplificaFracao(self):
        divisorComum = self.encontraMdc(self.__numerador, self.__denominador)
        self.__numerador = self.__numerador // divisorComum
        self.__denominador = self.__denominador // divisorComum

    def mesmaFracao(fracao1, fracao2):
        return (fracao1.numerador == fracao2.numerador) and (fracao1.denominador == fracao2.denominador)

    def __add__(self, outraFracao):
        novoNumerador = self.__numerador * outraFracao.denominador + outraFracao.numerador * self.__denominador
        novoDenominador = self.__denominador * outraFracao.denominador
        divisorComum = self.encontraMdc(novoNumerador, novoDenominador)
        return Fracao(novoNumerador//divisorComum, novoDenominador//divisorComum)
    
    def __str__(self):
        return str(self.__numerador) + "/" + str(self.__denominador)
    
if __name__ == "__main__":
    fracao1 = Fracao(10,4)
    fracao2 = Fracao(10,4)
    print(Fracao.mesmaFracao(fracao1, fracao2))
    print(fracao1 is fracao2)
    fracao2 = fracao1
    print(fracao1 is fracao2)

    print()

    fracao4 = Fracao(3,4)
    fracao5 = Fracao(5,6)
    print(fracao4 + fracao5) #invoca o __add__ por causa do +

    #== compara valores (conteúdo)
    #is compara a identidade (endereço de memória)