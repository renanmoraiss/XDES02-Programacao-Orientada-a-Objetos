n = int(input("Valor: "))
print('-' * 8)
print("Tabuada de {}:".format(n))
for i in range(11):
    if i == 0:
        continue
    print("{} x {:2} = {}".format(n, i, n * i))
print('-' * 8)