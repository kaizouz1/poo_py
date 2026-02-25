import os
def limpar():
    os.system("cls")
limpar()


class Aluno:
 def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2

 def calcular_media(self):
     media = (self.nota1 + self.nota2 / 2)
     return media
 
 def situacao(self):
    if self.calcular_media() >= 7:
       print(f"{self.nome} foi aprovado!")
    else:
       print(f"{self.nome} foi reprovado!")
media1 = Aluno("Osvaldo",13, 10)
media1.situacao()
media2 = Aluno("Gns", 5, 3)
media2.situacao()
 