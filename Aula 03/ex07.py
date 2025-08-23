import statistics as st

n = input("Número: ")
lista_numeros = []

while n != '0' and n:
    n = float(n)
    lista_numeros.append(n)
    n = input("Número: ")

tam_lista = len(lista_numeros)
if tam_lista > 0:
    print(lista_numeros)
    sum_numeros = 0
    for index in range(0, tam_lista):
        sum_numeros += lista_numeros[index]
    media_valores = (sum_numeros / tam_lista)
    print('Soma: {:.2f}'.format(sum_numeros))
    print("Média: {:.2f}".format(media_valores))
else:
    print("Lista sem elementos")

#ou
soma = sum(lista_numeros)
media = st.mean(lista_numeros) 
print('Soma: {:.2f}'.format(soma))
print('Média: {:.2f}'.format(media))