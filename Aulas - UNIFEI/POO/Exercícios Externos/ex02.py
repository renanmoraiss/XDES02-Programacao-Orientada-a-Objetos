class Pagamento:
    def calcular_total():
        pass

class PagamentoCartao(Pagamento):
    def __init__(self, valor, taxa):
        self.__valor = valor
        self.__taxa = taxa

    @property
    def valor(self):
        return self.__valor
    
    @property
    def taxa(self):
        return self.__taxa
    
    def calcular_total(self):
        return ("{}".format(self.__valor + self.__taxa))
    
class PagamentoBoleto(Pagamento):
    def __init__(self, valor, desconto):
        self.__valor = valor
        self.__desconto = desconto

    @property
    def valor(self):
        return self.__valor
    
    @property
    def desconto(self):
        return self.__desconto
    
    def calcular_total(self):
        return("{}".format(self.__valor - self.__desconto))
    
if __name__ == "__main__":
    pagamentos = [
        PagamentoCartao(100, 5),
        PagamentoBoleto(200, 20),
        PagamentoCartao(50, 2.5),
    ]

    for p in pagamentos:
        print(f"Total do pagamento: R${p.calcular_total()}")