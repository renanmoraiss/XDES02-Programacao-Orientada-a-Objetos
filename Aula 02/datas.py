from datetime import datetime, timedelta

data_corrente = datetime.now()
print("Dia de hoje: {}".format(data_corrente))

print("Dia: {}".format(data_corrente.day))
print("Mes: {}".format(data_corrente.month))
print("Ano: {}".format(data_corrente.year))

cem_dias = timedelta(days=100)
dia_passado = data_corrente - cem_dias
print("Um dia foi: {}".format(dia_passado))

nasc_renan = input('Data de nascimento (dd/mm/yyy): ')
data_nasc = datetime.strptime(nasc_renan, '%d/%m/%Y')
print("Data de nascimento: {}".format(data_nasc))

nasc_renan_dois = input('Data de nascimento (dd/mm/yyy): ')
data_nasc_dois = datetime.strptime(nasc_renan_dois, '%d/%m/%Y')
dia_nasc = data_nasc_dois.weekday()
match (dia_nasc):
    case 1:
        print("Domingo")
    case 2:
        print("Terça")
    case 3:
        print("Quarta")
    case 4:
        print("Quinta")
    case 5:
        print("Sexta")
    case 6:
        print("Sábado")
    case 7:
        print("Segunda")