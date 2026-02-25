import os
def limpar():
    os.system("cls")
limpar()


class Aluno():
 def __init__(self, nome, nota):
    self.nome = nome
    self.nota = nota
 
 def mostrar_nota(self):
    print(f"O aluno {self.nome} tirou nota {self.nota}")

aluno1 = Aluno("Kaizou", 10)
aluno1.mostrar_nota()