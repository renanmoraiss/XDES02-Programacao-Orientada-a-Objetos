#Código da P1 de POO

from datetime import datetime

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
class Caixao:
    def __init__(self, codigo, descricao, preco):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco(self):
        return self.__preco
    
class CoroaFlores:
    def __init__(self, codigo, descricao, preco):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco(self):
        return self.__preco
    
class VeiculoServico:
    def __init__(self, veiculo, kmSaida, kmChegada):
        self.__veiculo = veiculo
        self.__kmSaida = kmSaida
        self.__kmChegada = kmChegada

    @property
    def veiculo(self):
        return self.__veiculo
    
    @property
    def kmSaida(self):
        return self.__kmSaida
    
    @property
    def kmChegada(self):
        return self.__kmChegada

class Veiculo:
    def __init__(self, placa, custoKm):
        self.__placa = placa
        self.__custoKm = custoKm
    
    @property
    def placa(self):
        return self.__placa
    
    @property
    def custoKm(self):
        return self.__custoKm
    
class ServicoFunebre:
    def __init__(self, nro_servico, cliente, data, caixao):
        self.__nro_servico = nro_servico
        self.__cliente = cliente
        self.__data = data
        self.__caixao = caixao
        self.__listaCoroas = []
        self.__listaVeiculos = []

    @property
    def nro_servico(self):
        return self.__nro_servico
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def data(self):
        return self.__data
    
    @property
    def caixao(self):
        return self.__caixao
    
    @property
    def listaCoroas(self):
        return self.__listaCoroas
    
    @property
    def listaVeiculos(self):
        return self.__listaVeiculos
    
    def addVeiculo(self, veiculo):
        self.__listaVeiculos.append(veiculo)

    def addCoroa(self, coroa):
        self.__listaCoroas.append(coroa)

    def calculaGastoVeiculos(self):
        precoTotalCoroas = 0
        precoTotalVeiculo = 0
        precoParcialVeiculo = 0
        for coroa in self.__listaCoroas:
            precoTotalCoroas = precoTotalCoroas + coroa.preco
        for veic in self.__listaVeiculos:
            precoParcialVeiculo = veic.veiculo.custoKm * (veic.kmChegada - veic.kmSaida)
            precoTotalVeiculo = precoTotalVeiculo + precoParcialVeiculo
        print("Valor urna: {}".format(self.caixao.preco))
        print("Valor coroa(s): {}".format(precoTotalCoroas))
        print("Custo veículo(s): {}".format(precoTotalVeiculo))
        print("--------")
        print("Valor total: {}".format(self.caixao.preco + precoTotalCoroas + precoTotalVeiculo))
        print()

    def imprimeFatura(self):
        print("Nro Serviço: {}".format(self.__nro_servico))
        print("Cliente: {}".format(self.cliente.nome))
        self.calculaGastoVeiculos()
    
if __name__ == "__main__":
    caixao1 = Caixao(11, 'Urna Básica', 800)
    caixao2 = Caixao(12, 'Urna luxo', 1200)
    caixao3 = Caixao(13, 'Urna vip', 2000)

    coroa1 = CoroaFlores(101, 'Coroa de Flores P', 200)
    coroa2 = CoroaFlores(102, 'Coroa de Flores M', 270)
    coroa3 = CoroaFlores(103, 'Coroa de Flores G', 330)

    rebecao1 = Veiculo('ABC2D56', 5)
    rebecao2 = Veiculo('CBA1D65', 6)

    cliente1 = Cliente('Laura Cintra', '999777')
    cliente2 = Cliente('Mario Lima', '555888')

    servico1 = ServicoFunebre(1001, cliente1, datetime.now(), caixao2)
    servico1.addCoroa(coroa1)
    veicServ1 = VeiculoServico(rebecao1, 80456, 80486)
    servico1.addVeiculo(veicServ1)
    servico1.imprimeFatura()

    servico2 = ServicoFunebre(1002, cliente2, datetime.now(), caixao3)
    servico2.addCoroa(coroa2)
    servico2.addCoroa(coroa3)
    veicServ2 = VeiculoServico(rebecao1, 80486, 80510)
    veicServ3 = VeiculoServico(rebecao2, 55740, 55780)
    servico2.addVeiculo(veicServ2)
    servico2.addVeiculo(veicServ3)
    servico2.imprimeFatura()