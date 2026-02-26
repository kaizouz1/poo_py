import os 
def limpar():
    os.system("cls")
limpar()

class Carro:
 def __init__(self, modelo, velocidade):
    self.modelo = modelo
    self.velocidade = velocidade

 def acelerar(self, valor):
    