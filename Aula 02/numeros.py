import random #importando pacote

pi = 3.14159
print("pi = {}".format(pi))

dias_fev = 28
print("Tipo da variável 'dias_fev': {}".format(type(dias_fev)))
print("Fevereiro tem {} dias".format(dias_fev))
#print('Fevereiro tem ' + dias_fev + ' dias')
# -> errado, pois a combinação de números com strings não é permitida, então é necessário converter dias_fev para str.
print("Fevereiro tem " + str(dias_fev) + " dias")

#por padrão, a função input sempre retorna strings, então se for receber um número, é necessário converter no próprio input.
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
print("Primeiro número = {}; Segundo número: {}".format(n1, n2))
print("Soma de {} e {} = {}".format(n1, n2, n1 + n2))

print("Número aleatório entre 1 e 10: {}".format(random.randrange(1, 10)))
#randrange não inclui o limite superior, ou seja, pode imprimir de 1 até 9.