n1 = int(input("Primeiro nmr: "))
n2 = int(input("Segundo nmr: "))
soma = n1 + n2
subtracao = n1 - n2
produto = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
resto_divisao = n1 % n2
potencia = n1 ** n2
print("Soma = {};\nSubtração = {};\nProduto = {};\nDivisão = {:.2f};".format(soma, subtracao, produto, divisao))
print("Divisão inteira = {};\nResto da Divisão = {};\nPotencia = {}".format(divisao_inteira, resto_divisao, potencia))

name = input("Nome: ")
print("Seu nome é", end=' >>> ')
print("{}".format(name))