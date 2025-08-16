m = float(input("Distancia em metros: "))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print("{:.2f}m corresponde a:\n{:.2f}km\n{:.2f}hm\n{:.2f}dam\n{:.2f}dm\n{:.2f}cm\n{:.2f}mm".format(m, km, hm, dam, dm, cm, mm))