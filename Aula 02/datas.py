from datetime import datetime, timedelta
#datetime -> manipulação de datas.

data_atual = datetime.now() #pega a data de hoje.
                            #a função now retorna um objeto datetime
print("Data de hoje: {}".format(data_atual))

#funções para formatação de datas
print("Dia: {}".format(data_atual.day))
print("Mes: {}".format(data_atual.month))
print("Ano: {}".format(data_atual.year))
print()

#timedelta é usado para definir um período de tempo.
cem_dias = timedelta(days=100) #defino um período de tempo de 100 dias
print("Período de tempo: {}".format(cem_dias))
passado = data_atual - cem_dias
print("Hoje é: {}".format(data_atual))
print("100 dias atrás é: {}".format(passado))
print()

data_nascimento = input("Data de nascimento (dd/mm/yyyy): ") 
#input devolve datas como strings, então é necessário converter:
data = datetime.strptime(data_nascimento, '%d/%m/%Y') #converte string para data
print("Voce nasceu em {}".format(data))
um_dia = timedelta(days=1)
vespera_nascimento =  data - um_dia
print("Véspera do nascimento: {}".format(vespera_nascimento))