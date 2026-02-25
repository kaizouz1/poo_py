import os
def limpar():
    os.system("cls")
limpar()

class Musica:
 def __init__(self, titulo, artista):
    self.titulo = titulo
    self.artista = artista
 
 def tocar(self):
    print(f"Tocando {self.titulo} de {self.artista}")

musica1 = Musica("De onde eu venho", "Brandão")
musica1.tocar()