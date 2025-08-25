cotacao_dolar = 3.27
dinheiro_na_carteira = float(input("Quanto de $$ voce tem na carteira: "))
dolar_para_comprar = (dinheiro_na_carteira / cotacao_dolar)
print("Com R${:.2f} voce consegue comprar US${:.2f}".format(dinheiro_na_carteira, dolar_para_comprar))