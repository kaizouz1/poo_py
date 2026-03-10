import os 
def limpar():
    os.system("cls")
limpar()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}")
    
class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome} esta estudando")
        
class Professor(Pessoa):
    
    def ensinar(self):
        print(f"{self.nome} esta ensinando")

a = Aluno("Kaizou", 20)
p = Professor("Ana", 35)

a.apresentar()
a.estudar()
