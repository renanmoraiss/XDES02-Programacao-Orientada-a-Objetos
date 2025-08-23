import math
import random

n1 = int(input("Número: "))
raiz_n1 = math.sqrt(n1)
print("A raiz quadrada de {} é {:.2f}".format(n1, raiz_n1))
print("Arredondada para cima: {}".format(math.ceil(raiz_n1)))
print("Arredondada para baixo: {}".format(math.floor(raiz_n1)))

n2 = random.random() #por padrão, gera um float entre 0 e 1
print(n2)

n3 = random.randint(1, 20) #gera um int entre 1 e 20
print(n3) 