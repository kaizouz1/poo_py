import os
def limpar():
    os.system("cls")
limpar()


class Professor:
 def __init__(self, nome, disciplina):
    self.nome = nome
    self.disciplina = disciplina
  
 def lecionar(self):
  print(f"O professor {self.nome} da aula de {self.disciplina}")

professor1 = Professor("Girafales", "Matemática")
professor1.lecionar()