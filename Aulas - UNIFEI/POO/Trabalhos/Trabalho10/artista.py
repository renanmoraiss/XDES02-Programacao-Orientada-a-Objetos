import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Artista:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class LimiteInsereArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Cadastrar Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack(pady=10)
        self.frameButton.pack(pady=5)

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=25)
        self.inputNome.pack(side="left")

        self.buttonCria = tk.Button(self.frameButton, text="Enter")
        self.buttonCria.pack(side="left", padx=5)
        self.buttonCria.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left", padx=5)
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left", padx=5)
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlArtista:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaArtistas = []

    def insereArtistas(self):
        self.limiteIns = LimiteInsereArtista(self)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get().strip()
        if nome == "":
            self.limiteIns.mostraJanela('Erro', 'O nome do artista não pode estar vazio.')
            return

        for artista in self.listaArtistas:
            if artista.nome.lower() == nome.lower():
                self.limiteIns.mostraJanela('Erro', 'Esse artista já está cadastrado.')
                return

        novo = Artista(nome)
        self.listaArtistas.append(novo)
        self.limiteIns.mostraJanela('Sucesso','Artista "{}" cadastrado'.format(nome))
        self.limiteIns.destroy()

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def mostraArtistas(self):
        nomeBusca = simpledialog.askstring("Consulta Artista", "Nome do artista para consultar:")
        if not nomeBusca:
            return

        artistaEncontrado = next((art for art in self.listaArtistas if art.nome.lower() == nomeBusca.lower()), None)
        if not artistaEncontrado:
            messagebox.showinfo('Resultado','O artista "{}" não foi encontrado.'.format(nomeBusca))
            return

        albunsArtista = [alb for alb in self.ctrlPrincipal.ctrlAlbum.listaAlbuns
                         if (isinstance(alb.artista, str) and alb.artista.lower() == artistaEncontrado.nome.lower())
                         or (hasattr(alb.artista, "nome") and alb.artista.nome.lower() == artistaEncontrado.nome.lower())]

        if not albunsArtista:
            msg = 'O artista "{}" não possui álbuns cadastrados.'.format(artistaEncontrado.nome)
            messagebox.showinfo('Resultado', msg)
            return

        strArtista = 'Artista: {}\n\n'.format(artistaEncontrado.nome)
        for album in albunsArtista:
            strArtista += 'Álbum: {} ({})\n'.format(album.titulo, album.ano)
            for musica in album.musicas:
                strArtista += '   {}\n'.format(musica.titulo)
            strArtista += '\n'

        messagebox.showinfo('Consulta de Artista', strArtista)