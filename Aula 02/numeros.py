import random

pi = 3.1415
print(pi)

dias_fev = 28
print("Fevereiro tem {} dias".format(dias_fev))

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
print("Primeiro número = {}; Segundo número: {}".format(n1, n2))
print("Soma de {} e {} = {}".format(n1, n2, n1 + n2))

print("Número random entre 1 e 10: {}".format(random.randrange(1, 10)))


#Exercício 02 (gerar um random entre dois extremos inseridos pelo usuário)
n3 = int(input("Intervalo: "))
n4 = int(input("Intervalo: "))

if n3 < n4:
    print(random.randrange(n3, n4))
elif n4 < n3:
    print(random.randrange(n4, n3))
else:
    print("{} e {} são iguais".format(n3, n4))