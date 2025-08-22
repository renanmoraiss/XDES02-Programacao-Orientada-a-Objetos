string_um = input("Digite uma string: ")
string_copia = string_um
string_um = string_um.lower()
string_um = string_um.replace(' ', '') #tiro os espaços vazios (p n bugar em frases)

string_dois = string_um[::-1] #slice de trás p frente (inverte a string)

if (string_um == string_dois):
    print('{} é um palíndromo'.format(string_copia))
else:
    print('{} não é um palíndromo'.format(string_copia))