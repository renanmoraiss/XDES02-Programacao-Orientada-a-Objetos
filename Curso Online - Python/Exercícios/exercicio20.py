import random

aluno_um = input("Nome do primeiro aluno: ")
aluno_dois = input("Nome do segundo aluno: ")
aluno_tres = input("Nome do terceiro aluno: ")
aluno_quatro = input("Nome do quarto aluno: ")

lista_alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
random.shuffle(lista_alunos) #random.shuffle embaralha a lista
print(lista_alunos) 