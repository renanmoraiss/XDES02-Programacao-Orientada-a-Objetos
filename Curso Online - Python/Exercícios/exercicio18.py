import math

ang = int(input("Valor do angulo: "))
rad = math.radians(ang)

sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print("O angulo de {}° tem SEN: {:.2f}; COS: {:.2f} e TAN: {:.2f}".format(ang, sin, cos, tan))