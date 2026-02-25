import os
def limpar():
    os.system("cls")
limpar()




class Filme:
 def __init__(self, titulo, ano):
    self.titulo = titulo
    self.ano = ano 

 def detalhe(self):
    print(f"O filme {self.titulo} foi lançado em {self.ano}")
filme1 = Filme("Caçadores de Trolls: A Ascensão dos Titãs", "2021")
filme1.detalhe()