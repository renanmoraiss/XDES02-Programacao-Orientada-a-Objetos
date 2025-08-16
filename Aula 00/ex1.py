primeira_string = input("Digite a primeira frase: ")
segunda_string = input("Digite a segunda frase: ")
verificar_subtring = segunda_string in primeira_string
print(verificar_subtring)

if segunda_string in primeira_string:
    print(True)