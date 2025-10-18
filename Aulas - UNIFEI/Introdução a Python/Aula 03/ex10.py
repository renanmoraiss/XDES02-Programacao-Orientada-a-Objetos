def converte_seg(horas, minutos, segundos):
    seg_total = (horas * 3600) + (minutos * 60) + segundos
    return seg_total

def converte_hrs_min_seg(segundos_total):
    horas = (segundos_total // 3600)
    minutos = ((segundos_total - (horas * 3600)) // 60)
    segundos = segundos_total - ((horas * 3600) + (minutos * 60))
    print('O usuário ficou {} h {} min {} seg conectado na internet'.format(horas, minutos, segundos))

# quando o usuário entrou na internet
print("Entrada na internet:")
horas_entrada = int(input("Hora de entrada: "))
minutos_entrada = int(input("Minuto de entrada: "))
segundos_entrada = int(input("Segundo de entrada: "))

# quando o usuário saiu da internet
print("\nSaída da internet:")
horas_saida = int(input("Hora de saída: "))
minutos_saida = int(input("Minuto de saída: "))
segundos_saida  = int(input("Segundo de saída: "))

#desconsidere a hipótese de que a desconexão tenha ocorrido após a meia-noite.

seg_total_entrada = converte_seg(horas_entrada, minutos_entrada, segundos_entrada) #converter os dados de entrada para segundos
seg_total_saida = converte_seg(horas_saida, minutos_saida, segundos_saida) #converter os dados de saída para segundos

seg_total = seg_total_saida - seg_total_entrada
converte_hrs_min_seg(seg_total)