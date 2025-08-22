#Listas são coleções de items
nomes = ['Pedro', 'Marina']
notas = []
notas.append(9.2)
notas.append(8.7)
print(nomes)
print(notas)

comidas = ['maça', 'banana']
tam = len(comidas) #pega o tamanho da lista (número de elementos)
print("Tamanho de 'comidas': {}'".format(tam))
comidas.insert(0, 'arroz') #insere 'arroz' com índice 0 na lista
print(comidas)
comidas.sort() #ordena por número ou ordem alfabética
print(comidas)

univsersidades = ['UNIFEI', 'USP', 'UNICAMP']
top_universidade = univsersidades[:1] #obtém o primeiro elemento da lista, mesma coisa que [0:1]
print(univsersidades)
print(top_universidade)

numeros = list(range(11))
print(numeros)
tam = len(numeros)
print('Tamanho: {}'.format(tam))
inserir = int(input('Digite um inteiro para inserir em números: '))
numeros.insert((tam + 1), inserir)
new_tam = len(numeros)
print(numeros)
print('Novo tamanho: {}'.format(new_tam))