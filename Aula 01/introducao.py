print("Hello, World")
print()

nome = input("Digite seu nome: ")
print("Nome: " + nome)
print()

sobrenome = input("Digite seu sobrenome: ")
print("Sobrenome: " + sobrenome)
print()

nome_completo = nome + ' ' + sobrenome
print("Nome completo: " + nome_completo)
print()

print("Nome Maiúsculo: " + nome_completo.upper())
print("Nome Minúsculo: " + nome_completo.lower())
print("Apenas a primeira letra maiúscula: " + nome_completo.capitalize())
print("'a' aparece " + str(nome_completo.count('a')) + " vezes em " + nome_completo)

string1 = "Eu amo Itajubá"
res = "Itajubá" in string1
print(res)