import os 
def limpar():
    os.system("cls")
limpar()

class Personagem:
    def __init__(self, nome):
        self.nome = nome
    
    def atacar():
     return ("Esta atacando")
    

class Guerreiro(Personagem):
   def atacar(self):
      return (f"O guerreiro {self.nome} está atacando com sua nichirin")
   
class Mago(Personagem):
   def atacar(self):
      return (f"O mago {self.nome} está usando sua magia das trevas")
   

guerreiro1 = Guerreiro("Kaizouz1")
print(guerreiro1.atacar())

mago1 = Mago("Rafaelsantt")
print(mago1.atacar())