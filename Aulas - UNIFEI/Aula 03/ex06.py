str_um = input("Digite uma string: ")
str_um_copia = str_um
str_um = str_um.lower()
str_um = str_um.replace(' ', '') #tiro os espaços vazios (p n bugar em frases)

str_nova = str_um[::-1] #slice de trás p frente (inverte a string)

if (str_um == str_nova):
    print('{} é um palíndromo'.format(str_um_copia))
else:
    print('{} não é um palíndromo'.format(str_um_copia))

#ou

str_dois = input("Digite uma string: ")
str_dois_copia = str_dois
str_dois = str_dois.lower()
str_dois = str_dois.replace(' ', '')
tam_str = len(str_dois)
palindromo = True
for i in range(0, int(tam_str / 2)):
    if str_dois[i] != str_dois[tam_str - i - 1]:
        palindromo = False
if palindromo:
    print("{} é um palíndromo".format(str_dois_copia))
else:
    print("{} não é um palíndromo".format(str_dois_copia))