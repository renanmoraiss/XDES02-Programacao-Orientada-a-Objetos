total_pessoas = int(input("Deseja ler os dados de qtas pessoas: "))
nomes = [] #declaração de lista vazia
alturas = [] #declaração de lista vazia
for i in range(0, total_pessoas):
    nome = input("Nome da pessoa {}: ".format(i+1))
    nome = nome.capitalize()
    nomes.append(nome) #adiciona na lista de nomes

    altura = float(input("Altura da pessoa {}: ".format(i+1)))
    alturas.append(altura) #adiciona na lista de alturas

maior_altura = alturas[0]
index_maior = 0

menor_altura = alturas[0]
index_menor = 0

for i in range(0, int(len(alturas))):
    if alturas[i] > maior_altura:
        maior_altura = alturas[i]
        index_maior = i
    elif alturas[i] < menor_altura:
        menor_altura = alturas[i]
        index_menor = i

print("Pessoa mais alta: Nome = {}; Altura = {:.2f}".format(nomes[index_maior], maior_altura))
print("Pessoa mais baixa: Nome = {}; Altura = {:.2f}".format(nomes[index_menor], menor_altura))