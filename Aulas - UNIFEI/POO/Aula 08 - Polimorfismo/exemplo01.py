from abc import ABC, abstractmethod
class Documento(ABC):
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @abstractmethod
    def visualizar(self):
        pass

class Pdf(Documento):
    def visualizar(self):
        return 'Mostra no Adobe Acrobat'
    
class Word(Documento):
    def visualizar(self):
        return 'Mostra no Word'
    
if __name__ == "__main__":
    doc1 = Pdf("pdf1")
    doc2 = Word("Word1")
    doc3 = Pdf("pdf2")
    documentos = [doc1, doc2, doc3]
    for doc in documentos:
        print('{}: {}'.format(doc.nome, doc.visualizar()))