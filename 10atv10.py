import os
def limpar():
    os.system("cls")
limpar()



class Carro:
  def __init__(self, marca, ano):
    self.marca = marca
    self.ano = ano
  
  def mostrar_dados(self):
     print(f"Marca: {self.marca}\nAno: {self.ano}")
  
  def calcular_idade(self):
     self.idade = 2026 - self.ano
     print(f"Idade do carro: {self.idade}")
carro1 = Carro("Uno de escada", 1998)
carro1.mostrar_dados()
carro1.calcular_idade()