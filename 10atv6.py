import os
def limpar():
    os.system("cls")
limpar()

class Filme:
  def __init__(self, titulo, duracao):
   self.titulo = titulo
   self.duracao = duracao

  def eh_longo(self):
    if self.duracao >= 120:
     print(f"Filme:{self.titulo}\nDuração:{self.duracao:}\nÉ longo? Sim")
    else: 
      print(f"Filme:{self.titulo}\nDuração:{self.duracao}\nÉ longo? Não")
   
filme1 = Filme("Gente grande 1", 102)
filme1.eh_longo()

  