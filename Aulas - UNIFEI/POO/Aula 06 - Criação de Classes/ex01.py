#Exercício da Aula 06

class Veiculo:
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    @property
    def marca(self):
        return self.__marca
    
    @property
    def cor(self):
        return self.__cor
    
    @property
    def motorLigado(self):
        return self.__motorLigado
    
    #método
    def ligaMotor(self):
        if (self.__motorLigado == False):
            self.__motorLigado = True
            print("Motor foi ligado")

    #método
    def desligaMotor(self):
        if (self.__motorLigado == True):
            self.__motorLigado = False
            print("Motor foi desligado")

    #método
    def mostraAtributos(self):
        print("{} {}".format(self.__marca, self.__cor))
        if (self.__motorLigado == True):
            print("Motor ligado")
        else:
            print("Motor desligado")

class Carro(Veiculo):
    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio

    @property
    def portaMalasCheio(self):
        return self.__portaMalasCheio
    
    #método
    def enchePortaMalas(self):
        if (self.__portaMalasCheio == False):
            self.__portaMalasCheio = True
            print("Porta malas foi cheio")

    #método
    def esvaziaPortaMalas(self):
        if (self.__portaMalasCheio == True):
            self.__portaMalasCheio = False
            print("Porta malas foi esvaziado")

    #método
    def mostraAtributos(self):
        super().mostraAtributos()
        if (self.__portaMalasCheio == True):
            print("Porta malas cheio")
        else:
            print("Porta malas vazio")

class Moto(Veiculo):
    def __init__(self, marca, cor, motorLigado, estilo):
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo

    @property
    def estilo(self):
        return self.__estilo
    
    #método
    def mostraAtributos(self):
        super().mostraAtributos()
        print("Estilo {}".format(self.__estilo))

if __name__ == "__main__":
    moto = Moto("Kawasaki", "Verde", False, "Trail")
    moto.ligaMotor()
    print("Atributos da Moto:")
    moto.mostraAtributos()
    print()
    print("Atributos do Carro:")
    carro = Carro("Civic", "Preto", False, False)
    carro.enchePortaMalas()
    carro.ligaMotor()
    carro.mostraAtributos()