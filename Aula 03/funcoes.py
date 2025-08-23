def primeira_letra(str):
    return str[0]

nome = input("Digite seu nome: ")
primeira_letra_nome = primeira_letra(nome)

sobrenome = input("Digite seu sobrenome: ")
primeira_letra_sobrenome = primeira_letra(sobrenome)

print("A primeira letra de '{}' é '{}'".format(nome, primeira_letra_nome))
print("A primeira letra de '{}' é '{}'".format(sobrenome, primeira_letra_sobrenome))