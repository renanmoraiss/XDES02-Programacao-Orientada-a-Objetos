name = input("Nome: ")
lista_nomes = []

while name != '0' and name:
    lista_nomes.append(name.capitalize())
    name = input("Nome: ")

tam_nomes = len(lista_nomes)
if tam_nomes > 0:
    print(lista_nomes)
    nome_pesquisa = input("Pesquisar nome: ")
    nome_pesquisa = nome_pesquisa.capitalize()
    
    verificacao = False
    index = 0
    
    for i in range(0, len(lista_nomes)):
        if nome_pesquisa == lista_nomes[i]:
            verificacao = True
            index = i
            break
        
    if (verificacao):
        print("O nome '{}' foi encontrado".format(nome_pesquisa))
        print('Localizado no índice {}'.format(index))
    else:
        print("O nome '{}' não foi encontrado".format(nome_pesquisa))
else:
    print("Lista sem elementos")