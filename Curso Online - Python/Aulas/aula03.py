n1 = float(input("Digite um valor: "))
print(n1)

n2 = bool(input("Digite outro valor: ")) #bool -> True or False
print(n2)

n3 = input("Digite algo: ")
if (n3.isnumeric()):
    print("{} é numérico".format(n3))
else:
    print("{} nn é numérico".format(n3))