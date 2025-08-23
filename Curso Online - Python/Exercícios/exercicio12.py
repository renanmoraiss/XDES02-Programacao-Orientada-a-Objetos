preco_produto = float(input("Preco do produto: "))
preco_com_desconto = (preco_produto - (preco_produto * 0.05))
print("O preco do produto era de R${:.2f} e foi para R${:.2f}".format(preco_produto, preco_com_desconto))
print("O preco caiu R${:.2f}".format(preco_produto - preco_com_desconto))