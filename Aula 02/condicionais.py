renda = float(input("Renda mensal: "))
if renda >= 1903.99:
    if renda <= 2826.65:
        aliquota = 7.5
        imposto = renda * (aliquota / 100)
    elif renda >= 2826.66 and renda <= 3751.05:
        aliquota = 15
        imposto = renda * (aliquota / 100)
    elif renda <= 3751.06 and renda <= 4654.68:
        aliquota = 22.5
        imposto = renda * (aliquota / 100)
    else:
        aliquota = 27.5 
        imposto = renda * (aliquota / 100)
else:
    aliquota = 0

if renda >= 1903.99:
    print("Com uma renda de {:.2f}, voce irá pagar {:.2f} de imposto".format(renda, imposto))
else:
    print("Com uma renda de {:.2f}, voce está isento de imposto".format(renda))
