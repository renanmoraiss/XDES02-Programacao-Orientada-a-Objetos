salario = float(input("Salario: "))
novo_salario = salario + (salario * 0.15)
print("Seu salario era de R${:.2f} e aumentou para R${:.2f}".format(salario, novo_salario))
print("O aumento foi de R${}".format(novo_salario - salario))