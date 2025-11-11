import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from musica import Musica

class Album:
    def __init__(self, titulo, artista, ano, musicas):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__musicas = musicas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def ano(self):
        return self.__ano

    @property
    def musicas(self):
        return self.__musicas

class LimiteInsereAlbum(tk.Toplevel):
    def __init__(self, controle, listaNomesArtistas):
        tk.Toplevel.__init__(self)
        self.geometry('420x460')
        self.title("Cadastrar Álbum")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameLista = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameTitulo.pack(pady=5)
        self.frameArtista.pack(pady=5)
        self.frameAno.pack(pady=5)
        self.frameMusica.pack(pady=5)
        self.frameLista.pack(pady=5)
        self.frameButton.pack(pady=10)

        self.labelTitulo = tk.Label(self.frameTitulo, text="Título: ")
        self.labelTitulo.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width=30)
        self.inputTitulo.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista, text="Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaArtista = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width=25, textvariable=self.escolhaArtista)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomesArtistas

        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelAno.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=10)
        self.inputAno.pack(side="left")

        self.labelMusica = tk.Label(self.frameMusica, text="Título da música: ")
        self.labelMusica.pack(side="left")
        self.inputMusica = tk.Entry(self.frameMusica, width=20)
        self.inputMusica.pack(side="left")

        self.labelFaixa = tk.Label(self.frameMusica, text="Nº faixa: ")
        self.labelFaixa.pack(side="left")
        self.inputFaixa = tk.Entry(self.frameMusica, width=5)
        self.inputFaixa.pack(side="left")

        self.buttonInsereMusica = tk.Button(self.frameMusica, text="Inserir Música")
        self.buttonInsereMusica.pack(side="left", padx=5)
        self.buttonInsereMusica.bind("<Button>", controle.insereMusica)

        self.labelLista = tk.Label(self.frameLista, text="Músicas adicionadas:")
        self.labelLista.pack()
        self.listbox = tk.Listbox(self.frameLista, width=40, height=6)
        self.listbox.pack()

        self.buttonCadastrar = tk.Button(self.frameButton, text="Enter")
        self.buttonCadastrar.pack(side="left", padx=5)
        self.buttonCadastrar.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left", padx=5)
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left", padx=5)
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlAlbum:
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlbuns = []

    def insereAlbuns(self):
        listaNomesArtistas = [art.nome for art in self.ctrlPrincipal.ctrlArtista.listaArtistas]
        listaNomesArtistas.append("Vários artistas")
        self.listaMusicas = []
        self.limiteIns = LimiteInsereAlbum(self, listaNomesArtistas)

    def insereMusica(self, event):
        tituloMusica = self.limiteIns.inputMusica.get().strip()
        nroFaixa = self.limiteIns.inputFaixa.get().strip()

        if tituloMusica == "" or nroFaixa == "":
            self.limiteIns.mostraJanela('Erro', 'Informe o título e o número da faixa.')
            return

        musica = Musica(tituloMusica, nroFaixa)
        self.listaMusicas.append(musica)
        self.limiteIns.listbox.insert(tk.END, "{} - {}".format(nroFaixa, tituloMusica))
        self.limiteIns.inputMusica.delete(0, tk.END)
        self.limiteIns.inputFaixa.delete(0, tk.END)

    def enterHandler(self, event):
        titulo = self.limiteIns.inputTitulo.get().strip()
        nomeArtista = self.limiteIns.escolhaArtista.get()
        ano = self.limiteIns.inputAno.get().strip()

        if titulo == "" or nomeArtista == "" or ano == "" or len(self.listaMusicas) == 0:
            self.limiteIns.mostraJanela('Erro', 'Preencha todos os campos e insira ao menos uma música.')
            return

        if nomeArtista == "Vários artistas":
            artista = "Vários artistas"
        else:
            artista = next((art for art in self.ctrlPrincipal.ctrlArtista.listaArtistas if art.nome == nomeArtista), None)
            if artista is None:
                self.limiteIns.mostraJanela('Erro', 'Artista não encontrado.')
                return

        album = Album(titulo, artista, ano, self.listaMusicas)
        self.listaAlbuns.append(album)
        self.limiteIns.mostraJanela('Sucesso','Álbum "{}" cadastrado.'.format(titulo))
        self.limiteIns.destroy()

    def mostraAlbuns(self):
        tituloBusca = tk.simpledialog.askstring("Consulta Álbum", "Título do álbum para consultar:")

        if not tituloBusca:
            return

        albumEncontrado = next((alb for alb in self.listaAlbuns if alb.titulo.lower() == tituloBusca.lower()), None)

        if not albumEncontrado:
            messagebox.showinfo('Resultado','Nenhum álbum com o título "{}" foi encontrado.'.format(tituloBusca))
            return

        if isinstance(albumEncontrado.artista, str):
            nome_artista = albumEncontrado.artista
        else:
            nome_artista = albumEncontrado.artista.nome

        strAlbum = 'Álbum: {}\nMúsicas:\n'.format(albumEncontrado.titulo)
        for musica in albumEncontrado.musicas:
            strAlbum +='  {} - {}\n'.format(musica.nroFaixa, musica.titulo)

        messagebox.showinfo('Resultado da Consulta', strAlbum)

    def clearHandler(self, event):
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputMusica.delete(0, len(self.limiteIns.inputMusica.get()))
        self.limiteIns.inputFaixa.delete(0, len(self.limiteIns.inputFaixa.get()))
        self.limiteIns.listbox.delete(0, tk.END)
        self.limiteIns.combobox.set("")
        self.listaMusicas = []

    def fechaHandler(self, event):
        self.limiteIns.destroy()