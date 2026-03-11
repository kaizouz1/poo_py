import os 
def limpar():
    os.system("cls")
limpar()


class Animal:
    def __init__(self, nome):
     self.nome = nome


class Cachorro(Animal):
   def falar(self):
      return print(f"{self.nome} disse au au")

class Gato(Animal):
   def falarg(self):
      return print(f"{self.nome} disse miau")

animal1 = Cachorro("Jorge")
animal1.falar()

animal2 = Gato("Antonio")
animal2.falarg()