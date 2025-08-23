def converte(hrs, min, seg): #converte horas, minutos e segundos para segundos.
    return (hrs * 3600) + (min * 60) + seg 

hora = int(input("Horas: "))
minuto = int(input("Minutos: "))
segundo = int(input("Segundos: "))

#chamando a função
total_segundo = converte(hora, minuto, segundo)

print("{} hora(s), {} minuto(s) e {} segundo(s) = {} segundos".format(hora, minuto, segundo, total_segundo))