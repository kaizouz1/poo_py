
import os 
def limpar():
    os.system("cls")
limpar()



class Veiculo:
    def __init__(self, marca):
     self.marca = marca

    def mover(self):
       print(f"{self.marca} moveu-se")
    

class Carro(Veiculo):
   def mover(self):
    return (f"O carro {self.nome} está movendo-se a 100km")

class Moto(Veiculo):
   def mover(self):
        return (f"A moto {self.nome} está movendo-se a 250km ")


carro1 = Veiculo("Bora volkswagen")
carro1.mover()

moto1 = Veiculo("Lander")
moto1.mover()