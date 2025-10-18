renda = float(input("Renda mensal: "))
if renda >= 1900:
    aliquota = 7.5
    imposto = renda * (aliquota / 100)
    print("Com uma renda mensal de {:.2f} reais, voce deve pagar {:.2f} reais de imposto".format(renda, imposto))
else:
    aliquota = 0
    print("Voce esta isento de pagar imposto")
print()

estado = 'SP'
cupom_desconto = True #variável booleana

#se há uma lista de valores para verificar, pode usar o operador in.
if estado in('SP', 'RJ', 'PR') and cupom_desconto: #ou if estado == 'RJ' or estado == 'SP':
    frete = 0
elif estado == 'MG':
    frete = 15
elif estado == 'ES':
    frete = 18
else: #default - demais estados.
    frete: 20
print("Frete = {}".format(frete))
#se apenas uma condição pode ocorrer, é possível usar um único if em um conjunto com um ou mais elif's.
#usando vários if's, mesmo que um seja verdadeiro, ele continua testando o resto.