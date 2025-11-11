import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog

class Playlist:
    def __init__(self, nome, musicas):
        self.__nome = nome
        self.__musicas = musicas

    @property
    def nome(self):
        return self.__nome

    @property
    def musicas(self):
        return self.__musicas

class LimiteInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaNomesArtistas):
        tk.Toplevel.__init__(self)
        self.geometry('400x320')
        self.title("Cadastrar Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack(pady=5)
        self.frameArtista.pack(pady=5)
        self.frameMusica.pack(pady=5)
        self.frameButton.pack(pady=10)

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=30)
        self.inputNome.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista, text="Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaArtista = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width=25, textvariable=self.escolhaArtista)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomesArtistas
        self.combobox.bind("<<ComboboxSelected>>", controle.mostraMusicasArtista)

        self.labelMusica = tk.Label(self.frameMusica, text="Clique para adicionar músicas:")
        self.labelMusica.pack()
        self.listbox = tk.Listbox(self.frameMusica, width=40, height=8)
        self.listbox.pack()
        self.listbox.bind("<Double-1>", controle.insereMusica)

        self.buttonCria = tk.Button(self.frameButton, text="Enter")
        self.buttonCria.pack(side="left", padx=5)
        self.buttonCria.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left", padx=5)
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraPlaylists:
    def __init__(self, str):
        messagebox.showinfo('Playlists Cadastradas', str)

class CtrlPlaylist:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPlaylists = []

    def inserePlaylists(self):
        self.listaMusicasSel = []
        listaNomesArtistas = [art.nome for art in self.ctrlPrincipal.ctrlArtista.listaArtistas]
        self.limiteIns = LimiteInserePlaylist(self, listaNomesArtistas)

    def mostraMusicasArtista(self, event):
        artistaSel = self.limiteIns.escolhaArtista.get()
        self.limiteIns.listbox.delete(0, tk.END)

        for album in self.ctrlPrincipal.ctrlAlbum.listaAlbuns:
            if album.artista.nome.strip().lower() == artistaSel.strip().lower():
                for musica in album.musicas:
                    self.limiteIns.listbox.insert(tk.END, "{} ({})".format(musica.titulo, album.titulo))

    def insereMusica(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        if musicaSel not in self.listaMusicasSel:
            self.listaMusicasSel.append(musicaSel)
            self.limiteIns.mostraJanela('Sucesso','Música "{}" adicionada à playlist.'.format(musicaSel))

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get().strip()
        if nome == "" or len(self.listaMusicasSel) == 0:
            self.limiteIns.mostraJanela('Erro', 'Informe o nome e adicione ao menos uma música.')
            return

        playlist = Playlist(nome, self.listaMusicasSel)
        self.listaPlaylists.append(playlist)
        self.limiteIns.mostraJanela('Sucesso','Playlist "{}" criada.'.format(nome))
        self.limiteIns.destroy()

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.listbox.delete(0, tk.END)
        self.limiteIns.combobox.set("")

    def mostraPlaylists(self):
        nomeBusca = tk.simpledialog.askstring("Consulta Playlist", "Nome da playlist para consultar:")

        if not nomeBusca:
            return

        playlistEncontrada = next((pl for pl in self.listaPlaylists if pl.nome.lower() == nomeBusca.lower()), None)

        if not playlistEncontrada:
            messagebox.showinfo('Resultado','Nenhuma playlist com o nome "{}" foi encontrada.'.format(nomeBusca))
            return

        strPlay = 'Playlist: {}\nMúsicas:\n'.format(playlistEncontrada.nome)
        for musica in playlistEncontrada.musicas:
            strPlay += '  - {}\n'.format(musica)

        messagebox.showinfo('Resultado da Consulta', strPlay)

    def fechaHandler(self, event):
        self.limiteIns.destroy()