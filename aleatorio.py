import os 
def limpar():
    os.system("cls")
limpar()

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        
    def apresentar(self):
        return print(f"Olá, meu nome é {self.nome}")
    
class Aluno(Pessoa):
    def estudar(self):
        return print(f"{self.nome} esta estudando")
        
class Professor(Pessoa):
    
    def ensinar(self):
        return print(f"{self.nome} esta ensinando")

a = Aluno("Kaizou", 20)
p = Professor("Ana", 35)

p.apresentar()
p.ensinar()


a.apresentar()
a.estudar()


