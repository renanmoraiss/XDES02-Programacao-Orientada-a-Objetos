for nome in ['Messi', 'Neymar', 'CR7']:
    print(nome)
print()

for index in range(0, 4): #final do range é exclusivo
    print(index)
print()

nomes = ['Jason', 'DiCaprio', 'Brad Pitt']
index = 0
tam_nomes = len(nomes)
while index < tam_nomes:
    print(nomes[index])
    index += 1 #atualiza o valor de index
print()

#strings são cadeias de caracteres
myName = 'Renan'
i = 1
for x in myName:
    print('{}o caractere: {}'.format(i, x))
    i += 1
print()

#Desconto de 20% nos precos
precos = [10, 15, 200, 50, 350, 500]
tam_precos = len(precos)
i = 0
while i < tam_precos:
    preco_atualizado = precos[i] - (precos[i] * 0.2)
    print("Preço antigo = {}; Preço novo = {}".format(precos[i], preco_atualizado))
    i += 1