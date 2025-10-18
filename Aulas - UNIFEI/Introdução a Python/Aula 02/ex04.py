renda = float(input("Renda mensal: "))
if renda >= 1903.99:
    if renda <= 2826.65:
        aliquota = 7.5
    elif renda <= 3751.05:
        aliquota = 15
    elif renda <= 4664.68:
        aliquota = 22.5
    else:
        aliquota = 27.5
    imposto = renda * (aliquota / 100)
    print("Com uma renda de {:.2f} reais, sua alíquota é de {}%".format(renda, aliquota))
    print("Com isso, voce deve pagar {:.2f} reais de imposto".format(imposto))
else:
    print("Com uma renda de {:.2f} reais, voce esta isento de pagar imposto".format(renda))