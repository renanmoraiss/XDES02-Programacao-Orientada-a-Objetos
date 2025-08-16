largura = float(input("Largura: "))
altura = float(input("Altura: "))
area = largura * altura
qtd_tinta = (area / 2)
print("Em uma área de {:.3f}m², voce irá precisar de {:.3f}l de tinta".format(area, qtd_tinta))