import os 
def limpar():
    os.system("cls")
limpar()


class Conta:
    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.__saldo = saldo

    # 5 Criando um Getter:

    def get_saldo(self):
     return self.__saldo 
    
    # 6:
    def set_saldo(self, valor):
        if valor < 0:
         print("Erro: o saldo não pode ser negativo.")
        else:
         self.saldo = valor
    
banco1 = Conta("Jorge", "173.493.542-83", 1000)
print(banco1.get_saldo())
# 4 Criando atributo privado
# A: O codigo da erro e o atributo não é acessado.
# B: Ocorreu pelo fato do atributo "saldo" está privado e inacessivel fora e dentro da classe.


# 6
print(banco1.set_saldo(500))
print(banco1.set_saldo(-100))

# A regra pede para nao permitir numeros negativos, entao a função verifica vaor > 0 

