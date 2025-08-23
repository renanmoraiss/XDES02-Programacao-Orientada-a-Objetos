def soma(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

res = soma(n1, n2, n3)
print('Soma:' , res)

def calculo_imc(peso, altura):
    IMC = peso / pow(altura, 2)
    return IMC

peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = calculo_imc(peso, altura)
print('Seu IMC é:' , imc)

name = input("Nome: ")
age = int(input("Idade: "))
weight = float(input("Peso: "))
print("nome: {}; idade: {}; peso: {}".format(name, age, weight))