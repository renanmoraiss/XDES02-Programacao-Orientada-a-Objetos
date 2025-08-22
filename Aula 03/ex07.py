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
    print("Média: {:.2f}".format(media_valores))
else:
    print("Lista sem elementos")