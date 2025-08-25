qtd_dias = int(input("Qts dias alugado: "))
qtd_km = float(input("Qts km rodados: "))
total = (qtd_dias * 60) + (0.15 * qtd_km)
print("Sabendo que voce alugou o carro por {} dias e percorreu {} km, o total será de R${:.2f}".format(qtd_dias, qtd_km, total))