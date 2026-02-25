import os
def limpar():
    os.system("cls")
limpar()


class Carro:
 def __init__(self, modelo, cor):
    self.modelo = modelo
    self.cor = cor

 def descrever(self):
    print(f"Carro modelo {self.modelo} na cor {self.cor}")
carro1 = Carro("fiat uno com escada", "branco")
carro1.descrever()