import os 
def limpar():
    os.system("cls")
limpar()


class Veiculo:
    def mover(self):
     print("O veículo está se movendo")
class Moto(Veiculo):
    pass
m = Moto()
m.mover()

# 1 - A classe moto herdou o método mover().
