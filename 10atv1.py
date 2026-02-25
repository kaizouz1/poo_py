import os
def limpar():
    os.system("cls")
limpar()

class Banco:
 def __init__(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo
 
 def depositar(self, saldo):
    self.saldo += saldo
 
 def exibir_saldo(self):
    print(f"Nome: {self.titular}")
    print(f"Saldo: {self.saldo:.2f}")

 def sacar(self, valor):
     print(f"Saldo da conta: {self.saldo:.2f}")
     if valor > self.saldo:
            print("Saldo insuficiente!")
     else: 
         self.saldo -= valor
         return (f"Saque de R$ {valor:.2f} realizado")
    
banco1 = Banco("Kaizou", 15000)
banco1.depositar(10)
print(banco1.sacar(10000))
banco1.exibir_saldo()

