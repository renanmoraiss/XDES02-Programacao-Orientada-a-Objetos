dicionario = {'Brasil':'Portugues', 'Mexico':'Espanhol', 'Alemanha':'Alemao'}
print('No Brasil se fala {}'.format(dicionario['Brasil']))
print('No Mexico se fala {}'.format(dicionario['Mexico']))
print('Na Alemanha se fala {}'.format(dicionario['Alemanha']))
print()

pessoa = {'nome':'Renan', 'sobrenome':'Morais'}
print("Nome: {} {}".format(pessoa['nome'], pessoa['sobrenome']))
pessoa['curso_unifei'] = 'SIN'
print("Nome: {} {}; Curso: {}".format(pessoa['nome'], pessoa['sobrenome'], pessoa['curso_unifei']))
pessoa['idade'] = 18
print("Nome: {} {}; Curso: {}; Idade: {}".format(pessoa['nome'], pessoa['sobrenome'], pessoa['curso_unifei'], pessoa['idade']))
print(pessoa)
print('Idade: {}'.format(pessoa['idade']))
print('Curso: {}'.format(pessoa['curso_unifei']))

#Dicionários x Listas (DIFERENÇA)
#Dicionários armazenam pares 'chave / valor'. E acessamos os valores usando a chave, e não índice.
#Listas são baseadas em índices, que começam no índice zero. Acessamos os elementos usando o índice.