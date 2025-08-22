from datetime import datetime

data_nasc = input("Data de nascimento (dd/mm/yyyy): ")
data = datetime.strptime(data_nasc, '%d/%m/%Y')
day = data.weekday()
match day:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta feira")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")