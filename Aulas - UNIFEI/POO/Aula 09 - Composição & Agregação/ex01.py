#Exercício da Aula 09

class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def albuns(self):
        return self.__albuns
    
    @property
    def musicas(self):
        return self.__musicas
    
    def adicionaAlbum(self, album):
        self.__albuns.append(album)

    def adicionaMusica(self, musica):
        self.__musicas.append(musica)

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__faixas = []

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
    def faixas(self):
        return self.__faixas
    
    def adicionaFaixa(self, titulo, artista=None):
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas)
        musica = Musica(titulo, artista, self, nroFaixa)
        self.__faixas.append(musica)

class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def album(self):
        return self.__album
    
    @property
    def nroFaixa(self):
        return self.__nroFaixa
    
class Playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
    
    def adicionaMusica(self, musica):
        self.__musicas.append(musica)

    def exibirPlaylist(self):
        for musica in self.__musicas:
            print("{} | {}".format(musica.titulo, musica.artista.nome))

if __name__ == "__main__":
    listaAlbuns = []
    art1 = Artista('Coldplay')
    album1 = Album('Mylo Xyloto', art1, 2011)
    album1.adicionaFaixa('Paradise')
    album1.adicionaFaixa('Hurts Like Heaven')
    album1.adicionaFaixa('Charlie Brown')
    listaAlbuns.append(album1)

    album2 = Album('A Head Full of Dreams', art1, 2015)
    album2.adicionaFaixa('A Head Full of Dreams')
    album2.adicionaFaixa('Birds')
    album2.adicionaFaixa('Everglow')
    listaAlbuns.append(album2)

    art2 = Artista('Skank')
    album3 = Album('Siderado', art2, 1998)
    album3.adicionaFaixa('Resposta')
    album3.adicionaFaixa('Saideira')
    album3.adicionaFaixa('Romance Noir')
    listaAlbuns.append(album3)

    playlist1 = Playlist("Músicas do álbum Mylo Xyloto")
    print(playlist1.nome)
    for faixa in album1.faixas:
        playlist1.adicionaMusica(faixa)
    playlist1.exibirPlaylist()

    print()

    playlist2 = Playlist("Todas as músicas do Coldplay")
    print(playlist2.nome)
    for faixa in album1.faixas:
        playlist2.adicionaMusica(faixa)
    for faixa in album2.faixas:
        playlist2.adicionaMusica(faixa)
    playlist2.exibirPlaylist()

    print()

    playlist3 = Playlist("Uma música de cada álbum")
    playlist3.adicionaMusica(album1.faixas[0])
    playlist3.adicionaMusica(album2.faixas[0])
    playlist3.adicionaMusica(album3.faixas[0])
    print(playlist3.nome)
    playlist3.exibirPlaylist()