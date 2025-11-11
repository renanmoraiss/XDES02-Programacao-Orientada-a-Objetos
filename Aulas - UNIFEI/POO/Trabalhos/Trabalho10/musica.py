import tkinter as tk
from tkinter import messagebox

class Musica:
    def __init__(self, titulo, nroFaixa):
        self.__titulo = titulo
        self.__nroFaixa = nroFaixa

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def nroFaixa(self):
        return self.__nroFaixa

class LimiteInsereMusicas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Música")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameNroFaixa = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameNroFaixa.pack()
        self.frameButton.pack()
      
        self.labelTitulo = tk.Label(self.frameTitulo, text="Título: ")
        self.labelNroFaixa = tk.Label(self.frameNroFaixa, text="Nº da faixa: ")
        self.labelTitulo.pack(side="left")
        self.labelNroFaixa.pack(side="left")

        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
        self.inputNroFaixa = tk.Entry(self.frameNroFaixa, width=20)
        self.inputNroFaixa.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraMusicas():
    def __init__(self, str):
        messagebox.showinfo('Lista de músicas', str)

class CtrlMusica:
    def __init__(self):
        self.listaMusicas = []

    def getListaMusicas(self):
        return self.listaMusicas

    def getMusica(self, tituloMusica):
        for musica in self.listaMusicas:
            if musica.titulo == tituloMusica:
                return musica
        return None

    def getListaTitulosMusicas(self):
        listaTitulos = []
        for musica in self.listaMusicas:
            listaTitulos.append(musica.titulo)
        return listaTitulos

    def insereMusicas(self):
        self.limiteIns = LimiteInsereMusicas(self)

    def mostraMusicas(self):
        str = 'Título -- Nº Faixa\n'
        for musica in self.listaMusicas:
            str += musica.titulo + ' -- ' + musica.nroFaixa + '\n'
        self.limiteLista = LimiteMostraMusicas(str)

    def enterHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get()
        nroFaixa = self.limiteIns.inputNroFaixa.get()
        musica = Musica(titulo, nroFaixa)
        self.listaMusicas.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Música cadastrada.')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputNroFaixa.delete(0, len(self.limiteIns.inputNroFaixa.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()