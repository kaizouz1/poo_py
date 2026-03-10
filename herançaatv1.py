import os
def limpar():
    os.system("cls")
limpar()

# Excercicio 1
class Animal:
    def falar(self):
     print("O animal faz um som")

class Cachorro(Animal):
  pass
  
dog = Cachorro()
dog.falar()

# 1 - Qual é a classe pai?
# - Animal.

# 2 - Qual é a classe filha?
# - Cachorro

# 3 - Por que o cachorro consegue usar o método falar()?
# - porque a classe cachorro foi chamada no finaldo codigo junto do método.

# Excercicio 2
class Gato(Animal):
    pass
g = Gato()
g.falar()

# 1 - o método falar() foi criado na classe Gato ou herdado?
# - Foi herdado.

# Excercicio 3
class Pessoa:
 def __init__(self, nome):
    self.nome = nome
class Aluno(Pessoa):
 pass
a = Aluno("joao")
print(a.nome)

# 1 - onde o atributo nome foi criado?
# - Na classe pessoa

# 2 - por que a classe Aluno consegue usar esse atributo
# - porque a classe pessoa foi chamada na classe Aluno



