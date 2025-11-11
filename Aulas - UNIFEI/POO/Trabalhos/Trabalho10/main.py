import tkinter as tk
import artista as art
import album as alb
import playlist as play
import musica as mus

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('350x200')
        self.root.title("Sistema de Músicas")

        self.menubar = tk.Menu(self.root)

        self.artistaMenu = tk.Menu(self.menubar)
        self.artistaMenu.add_command(label="Cadastrar", 
                                     command=self.controle.cadastraArtista)
        self.artistaMenu.add_command(label="Consultar", 
                                     command=self.controle.consultaArtista)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        self.albumMenu = tk.Menu(self.menubar)
        self.albumMenu.add_command(label="Cadastrar", 
                                   command=self.controle.cadastraAlbum)
        self.albumMenu.add_command(label="Consultar", 
                                   command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label="Álbum", menu=self.albumMenu)

        self.playlistMenu = tk.Menu(self.menubar)
        self.playlistMenu.add_command(label="Cadastrar", 
                                      command=self.controle.cadastraPlaylist)
        self.playlistMenu.add_command(label="Consultar", 
                                      command=self.controle.consultaPlaylist)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlMusica = mus.CtrlMusica()
        self.ctrlArtista = art.CtrlArtista(self)
        self.ctrlAlbum = alb.CtrlAlbum(self)
        self.ctrlPlaylist = play.CtrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.mainloop()

    def cadastraArtista(self):
        self.ctrlArtista.insereArtistas()

    def consultaArtista(self):
        self.ctrlArtista.mostraArtistas()

    def cadastraAlbum(self):
        self.ctrlAlbum.insereAlbuns()

    def consultaAlbum(self):
        self.ctrlAlbum.mostraAlbuns()

    def cadastraPlaylist(self):
        self.ctrlPlaylist.inserePlaylists()

    def consultaPlaylist(self):
        self.ctrlPlaylist.mostraPlaylists()

if __name__ == '__main__':
    c = ControlePrincipal()