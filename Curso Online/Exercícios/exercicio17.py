from math import pow, sqrt

co = float(input("Comprim do Cateto Op.: "))
ca = float(input("Comprimento do Cateto Ad.: "))
h = sqrt(pow(co, 2) + pow(ca, 2))
print("CO: {:.2f}; CA: {:.2f}; H: {:.2f}".format(co, ca, h))