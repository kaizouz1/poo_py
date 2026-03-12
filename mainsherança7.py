import os
def limpar():
    os.system("cls")
limpar()

from herança7 import Veiculo, Carro, Moto


carro1 = Veiculo("Bora volkswagen")
carro1.mover()

moto1 = Veiculo("Lander")
moto1.mover()