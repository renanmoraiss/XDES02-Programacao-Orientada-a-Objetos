from datetime import datetime

day = int(input("DD: "))
month = int(input("MM: "))
year = int(input("YYYY: "))
print("{}/{}/{}".format(day, month, year))

#ou
data = input("Data de nascimento (dd/mm/yyyy): ")
data_nasc = datetime.strptime(data, '%d/%m/%Y')
print(data_nasc)