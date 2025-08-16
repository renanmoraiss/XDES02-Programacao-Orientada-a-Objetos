n1 = float(input("Sua nota na N1: "))
n2 = float(input("Sua nota na N2: "))
MF = (n1 + n2) / 2
if MF >= 6.0:
    print("Aluno aprovado com {:.2f} de média".format(MF))
elif MF >= 3.0 and MF <= 6.0:
    print("Aluno de substitutiva com {:.2f} de média".format(MF))
else:
    print("Aluno reprovado com {:.2f} de média".format(MF))