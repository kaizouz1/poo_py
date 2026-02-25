import os
def limpar():
    os.system("cls")
limpar()


class Livro: 
 def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor

 def resumo(self):
    print(f"O Mangá {self.titulo} foi escrito por {self.autor}")

livro1 = Livro("Boruto Two Blue Vortex", "Masashi Kishimoto / Mikio Ikemoto")
livro1.resumo()
