import random

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 < n2:
    print(random.randrange(n1, n2))
elif n2 < n1:
    print(random.randrange(n2, n1))
else:
    print("{} e {} são iguais".format(n1, n2))