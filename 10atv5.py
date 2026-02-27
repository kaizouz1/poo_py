import os 
def limpar():
    os.system("cls")
limpar()


class Livro:

 def __init__(self, titulo, autor, paginas):
   self.titulo = titulo
   self.autor = autor
   self.paginas = paginas

 def detalhes(self):
   print(f"Título: {self.titulo}\nAutor:{self.autor}\nPáginas")

 def longo(self):
   if self.paginas > 300:
     print(f"{self.titulo} possui mais de 300 páginas!")
     return True
   else:
     print(f"{self.titulo} não possui mais de 300 páginas")
     return False
   
livro1 = Livro("Boruto Two Blue Vortex", "kaizou", 184)
livro1.detalhes()
livro1.longo()