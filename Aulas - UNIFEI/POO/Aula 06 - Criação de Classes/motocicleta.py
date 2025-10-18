#Criando uma classe

class Motocicleta:
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    #método de instancia
    def ligaMotor(self):
        if self.__motorLigado == True:
            print("O motor já esta ligado!")
        else:
            self.__motorLigado = True
            print("O motor acaba de ser ligado!")

    #método que não modifica atributo
    def mostraAtributos(self):
        print('Esta motocicleta é uma {} {}'.format(self.__marca, self.__cor))
        if(self.__motorLigado == True):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')

moto1 = Motocicleta('Honda', 'Vermelha', False)
moto1.mostraAtributos()
print()
moto1.ligaMotor()
print()
moto1.mostraAtributos()
print()
moto1.ligaMotor()