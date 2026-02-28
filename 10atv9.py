import os
def limpar():
    os.system("cls")
limpar()
from time import sleep

class Jogo:
 def __init__(self, nome):
  self.nome = nome
  self.nivel = 1

 def subir_nivel(self):
  self.nivel += 1
  print(f"{self.nome} subiu para o nivel {self.nivel}")

jogador1 = Jogo("Kaizouz1")
jogador1.subir_nivel()
sleep(2)
jogador1.subir_nivel()
