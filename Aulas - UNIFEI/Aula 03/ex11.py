def converte(total_segundo): #converte segundos para horas, minutos e segundos.
    hora = (total_segundo // 3600)
    minuto = (total_segundo - (hora * 3600)) // 60
    segundo = (total_segundo - (hora * 3600 + minuto * 60))
    print("{} segundo(s) = {} hora(s), {} minuto(s) e {} segundo(s)".format(total_segundo, hora, minuto, segundo))

segundo = int(input("Total de segundos: "))
#chamando a função
converte(segundo)