import os
def limpar():
    os.system("cls")
limpar()


class Carro:
    def __init__(self, velocidade):
        self.velocidade = velocidade

carro = Carro(100)
carro.velocidade = 200
print(f"Carro: {carro.velocidade}")


class Carro2:
    def __init__(self, velocidade):
        self._velocidade = velocidade

carro = Carro2(100)
carro._velocidade = 200
print(f"Carro2: {carro._velocidade}")


class Carro3:
    def __init__(self, velocidade):
        self.__velocidade = velocidade

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, valor):
         valor >= 0, "Velocidade não pode ser negativa"
         self.__velocidade = valor
        

carro = Carro3(100)
carro.velocidade = 120
print(f"Carro3: {carro.velocidade}")


# A: Qual versão oferece maior controle?
# A Versão 3 (atributo privado com @property).


# b) Qual é mais adequada para sistemas profissionais?
# A Versão 3.


# C: porque ela segue os principios da Poo.






