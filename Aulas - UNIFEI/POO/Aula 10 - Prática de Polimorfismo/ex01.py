#Exercício da Aula 10

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, nome_correntista, saldo):
        self.__numero = numero
        self.__nome_correntista = nome_correntista
        self.__saldo = saldo
        self.__transacoes = []

    @property
    def numero(self):
        return self.__numero
    
    @property
    def nome_correntista(self):
        return self.__nome_correntista
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
    
    @property
    def transacoes(self):
        return self.__transacoes
    
    def depositar(self, valor, descricao):
        self.__saldo += valor
        self.__transacoes.append(Transacao("19/10/2025", valor, descricao))

    def retirar(self, valor, descricao):
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__transacoes.append(Transacao("19/10/2025", -valor, descricao))
            return True
        else:
            return False

    def adicionarTransacao(self, transacao):
        self.__transacoes.append(transacao)

    @abstractmethod
    def imprimirExtrato(self):
        pass

class ContaCorrente(Conta):
    def __init__(self, numero, nome_correntista, saldo, mensalidade):
        super().__init__(numero, nome_correntista, saldo)
        self.__mensalidade = mensalidade

    @property
    def mensalidade(self):
        return self.__mensalidade
    
    def retirar(self, valor, descricao):
        if valor <= self.saldo:
            self.saldo -= valor
            self.transacoes.append(Transacao("19/10/2025", -valor, descricao))
            return True
        else:
            return False

    def imprimirExtrato(self):
        print("=== Extrato - Conta Corrente ===")
        print("Número: {}".format(self.numero))
        print("Cliente: {}".format(self.nome_correntista))
        print("----------")
        for transacao in self.transacoes:
            print("Data: {} | {} | {}".format(transacao.data, transacao.descricao, transacao.valor))
        print("Mensalidade: {}".format(self.__mensalidade))
        print("Saldo atual: {}".format(self.saldo))

class ContaLimite(Conta):
    def __init__(self, numero, nome_correntista, saldo, limite):
        super().__init__(numero, nome_correntista, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite
    
    def retirar(self, valor, descricao):
        if valor <= self.saldo + self.__limite:
            self.saldo -= valor
            self.transacoes.append(Transacao("19/10/2025", -valor, descricao))
            return True
        else:
            return False

    def imprimirExtrato(self):
        print("=== Extrato - Conta com Limite ===")
        print("Número: {}".format(self.numero))
        print("Cliente: {}".format(self.nome_correntista))
        print("----------")
        for transacao in self.transacoes:
            print("Data: {} | {} | {}".format(transacao.data, transacao.descricao, transacao.valor))
        print("Limite disponível: {}".format(self.__limite))
        print("Saldo: {}".format(self.saldo))

class ContaPoupanca(Conta):
    def __init__(self, numero, nome_correntista, saldo, dia_aniversario):
        super().__init__(numero, nome_correntista, saldo)
        self.__dia_aniversario = dia_aniversario

    @property
    def dia_aniversario(self):
        return self.__dia_aniversario
    
    def imprimirExtrato(self):
        print("=== Extrato - Conta Poupança ===")
        print("Número: {}".format(self.numero))
        print("Cliente: {}".format(self.nome_correntista))
        print("----------")
        for transacao in self.transacoes:
            print("Data: {} | {} | {}".format(transacao.data, transacao.descricao, transacao.valor))
        print("Dia do aniversário: {}".format(self.__dia_aniversario))
        print("Saldo: {}".format(self.saldo))

class Transacao:
    def __init__(self, data, valor, descricao):
        self.__data = data
        self.__valor = valor
        self.__descricao = descricao

    @property
    def data(self):
        return self.__data
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def descricao(self):
        return self.__descricao
    
if __name__=="__main__":
    contas = []
    cc = ContaCorrente(1111, 'João Silva', 0, 30)
    cc.depositar(1000, 'Crédito salário')
    if cc.retirar(500, 'Pagto energia'):
        print('Saque de R$500,00 na conta {}'.format(cc.numero))
    else:
        print('Falha ao realizar saque de R$500,00 na conta {}'.format(cc.numero))
    if cc.retirar(700, 'PIX'):
        print('Saque de R$700,00 na conta {}'.format(cc.numero))
    else:
        print('Falha ao realizar saque de R$700,00 na conta {}'.format(cc.numero))
    contas.append(cc)
    print()
    cl = ContaLimite(2222, 'Ana Souza', 0, 1000)
    cl.depositar(1500, 'Crédito salário')
    if cl.retirar(1200, 'Pagto boleto'):
        print('Saque de R$1200,00 na conta {}'.format(cl.numero))
    else:
        print('Falha ao realizar saque de R$1200,00 na conta {}'.format(cl.numero))
    if cl.retirar(500, 'PIX'):
        print('Saque de R$500,00 na conta {}'.format(cl.numero))
    else:
        print('Falha ao realizar saque de R$500,00 na conta {}'.format(cl.numero))
    contas.append(cl)
    print()
    cp = ContaPoupanca(3333, 'João Silva', 0, 10)
    cp.depositar(1200, 'Econominas')
    if cp.retirar(400, 'Resgate 1'):
        print('Saque de R$400,00 na conta {}'.format(cp.numero))
    else:
        print('Falha ao realizar saque de R$500,00 na conta {}'.format(cp.numero))
    if cp.retirar(300, 'Resgate 2'):
        print('Saque de R$300,00 na conta {}'.format(cp.numero))
    else:
        print('Falha ao realizar saque de R$700,00 na conta {}'.format(cp.numero))
    contas.append(cp)
    print()
    for conta in contas:
        conta.imprimirExtrato()
        print()