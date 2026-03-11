import os 
def limpar():
    os.system("cls")
limpar()


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

class Aluno(Pessoa):
   def aprendendo(self):
        print(f"Me chamo {self.nome} e tenho {self.idade} anos")
        print(f"{self.nome} está aprendendo")

class Professor(Pessoa):
   def ensinando(self):
        print(f"eu me chamo {self.nome} e tenho {self.idade} anos")
        print(f"{self.nome} está ensinando!")
        



pessoa1 = Professor("Fernando", 46)
pessoa1.ensinando()

pessoa2 = Aluno("Kaizou", 16)
pessoa2.aprendendo()
