import os 
def limpar():
    os.system("cls")
limpar()


 
class Conta: 
    def __init__(self, saldo): 
        self.__saldo = saldo 
 
    @property 
    def saldo(self): 
        return self.__saldo 
 
    @saldo.setter 
    def saldo(self, valor): 
        if valor >= 0: 
            self.__saldo = valor 
        else: 
            print("Valor inválido") 

conta1 = Conta(1000) 
print(conta1.saldo) 
conta1.saldo = 800
print(conta1.saldo)
conta1.saldo = -500
print(conta1.saldo)

