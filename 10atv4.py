import os 
def limpar():
    os.system("cls")
limpar()

class Carro:
 def __init__(self, modelo, velocidade):
    self.modelo = modelo
    self.velocidade = velocidade

 def acelerar(self, valor):
    self.aceleracao = valor
    print(f"Uno de escada acelerou {self.aceleracao}Km")
    

 def freiar(self, freiou):
     self.freio = self.aceleracao - freiou
     print(f"uno de escada freiou {self.freio}km")

 def status(self):
    self.veloz = (self.velocidade + self.aceleracao) - self.freio
    print(f"Modelo: {self.modelo}\nVelocidade: {self.veloz:.2f}")
    
        

carro1 = Carro("Uno de escada", 0)
carro1.acelerar(100)
carro1.freiar(50)
carro1.status()

