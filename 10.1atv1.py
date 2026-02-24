import os 
def limpar():
    os.system("cls")
limpar()


class Cachorro: 
   def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
   
   def latir(self):
      return(f"{self.nome} disse auauau e tem {self.idade} anos")
cachorro1 = Cachorro("Adolfinho", 13)
print(cachorro1.latir())
# ------------
cachorro2 = Cachorro("Davi", 10)
print(cachorro2.nome)

