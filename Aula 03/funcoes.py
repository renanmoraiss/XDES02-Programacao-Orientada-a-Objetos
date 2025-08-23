from datetime import datetime

nome = 'Renan'
print('Tarefa concluída')
print(datetime.now())
print()

for i in range(0, 10):
    print(i)
print('Tarefa concluída')
print(datetime.now())
print()

#há uma repetição de código acima, portanto, é bom usar função para evitar isso.
def print_time():
    print('Tarefa concluída')
    print(datetime.now())
    print()

nome = 'Renan'
print_time()

for i in range(0, 10):
    print(i)
print_time()

#se eu quiser imprimir mensagens diferentes:
def print_time(mensagem): #agora, a função tem um parametro.
    print(mensagem)
    print(datetime.now())
    print()

nome = 'Renan'
print_time('Nome atribuído')

for i in range(0, 10):
    print(i)
print_time('Loop executado')

#Funções com retorno:
def first_letter(str): #função que retorna a primeira letra de uma string
    return str[0] #ou str[0:1]

name = input("Digite seu nome: ")
surname = input("Digite seu sobrenome: ")

#chamando as funções. E como elas retornam algo, eu devo igualar uma variável a chamada delas (assim como em C).
first_letter_name = first_letter(name)
first_letter_surname = first_letter(surname)

#imprimir o resultado
print("Inicial do nome '{}' é '{}'".format(name, first_letter_name))
print("Inicial do sobrenome '{}' é '{}'".format(surname, first_letter_surname))
print()

#Funções podem ter múltiplos parametros
def get_inicial(text, maiuscula):
    if maiuscula: #verifica se o booleano é True
        return text[0].upper()
    else:
        return text[0]

text = input("Digite seu nome: ")
inicial_text = get_inicial(text, False)
print("A inicial de '{}' é '{}'".format(text, inicial_text))
print()

#É possível especificar um valor default para um parametro
def get_last(str, last, maiuscula=True):
    if maiuscula:
        return str[last-1].upper()
    else:
        return str[last-1]
    
name = input("Digite seu nome: ")
last_name = get_last(name, len(name))
print("Nome: {}; Última letra: {}".format(name, last_name))
print()

#É possível especificar valores nomeando os parametros
def inicial(str, maiuscula):
    if maiuscula:
        return str[0].upper()
    else:
        return str[0]

nome = input("Digite seu nome: ")
#Quando os parametros são nomeados (como abaixo), eles podem aparecer em qualquer ordem.
inicial_nome = inicial(maiuscula=True, str=nome)
print("Nome: {}; Primeira letra: {}".format(nome, inicial_nome))