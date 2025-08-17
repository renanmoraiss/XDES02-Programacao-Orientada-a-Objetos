from math import pow, sqrt

co = float(input("Comprimento do CO: "))
ca = float(input("Comprimento do CA: "))
h = sqrt(pow(co, 2) + pow(ca, 2))
print("CO: {:.2f}; CA: {:.2f}; H: {:.2f}".format(co, ca, h))