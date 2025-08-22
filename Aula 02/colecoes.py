#Listas são coleções de itens
enxadristas = ['Carlsen', 'Nakamura']
rating = []
rating.append(2839) #adiciona novo item no final
rating.append(2807)
print(enxadristas)
print(rating)
print('Enxadrista: {}; Rating clássico: {}'.format(enxadristas[0], rating[0])) #coleções iniciam no índice zero
print('Enxadrista: {}; Rating clássico: {}'.format(enxadristas[1], rating[1]))
print()

#Arrays também são coleções de itens
from array import array
notas = array('d') #o argumento 'd' define qual tipo de dado o array vai armazenar, que nesse caso é double.
notas.append(10.0)
notas.append(9.5)
print(notas)
print(notas[0])
print()

#Arrays x Listas (DIFERENÇA)
#Arrays armazenam somente tipos simples como números, e todos os itens devem ser do mesmo tipo.
#Lists armazenam qualquer dado de qualquer tipo.

futebolistas = ['Benzema', 'Antony']
tam = len(futebolistas) #obtém o comprimento (número de itens)
print(futebolistas)
print("Comprimento = {}".format(tam))
futebolistas.insert(0, 'Cristiano Ronaldo') #insere um elemento
new_tam = len(futebolistas)
print(futebolistas)
print("Novo Comprimento = {}".format(new_tam))
futebolistas.sort() #ordena em ordem numérica e ordem alfabética (por padrão - crescente)
print('Ordem crescente {}'.format(futebolistas))

#se eu quiser ordenar na ordem reversa, devo usar o argumento reverse=True dentro dos () no sort.
futebolistas.sort(reverse=True)
print('Ordem reversa {}'.format(futebolistas))
print()

atores = ['Leonardo DiCaprio', 'Brad Pitt', 'Jason Statham']
atores_selecionados = atores[0:2] #obtém os dois primeiros itens
                            #[índice inicial(inclusivo):índice final(exclusivo)]
print(atores)
print(atores_selecionados)

atores_selecionados = atores[0::2] #0 é o índice inicial. Não tem índice final, ou seja, pega até o final. E o 2 é o passo, ou seja, ele pega de 2 em 2.
print(atores_selecionados)

atores_selecionados = atores[1:] #pega do índice 1 até o final
print(atores_selecionados)
print()

estrelas = [14, 17, 2, 4, 0, -2, 5, 9]
print(estrelas)
estrelas.sort()
print('Ordem crescente {}'.format(estrelas))
estrelas.sort(reverse=True)
print('Ordem decrescente {}'.format(estrelas))