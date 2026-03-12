import os 
def limpar():
    os.system("cls")
limpar()



class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self._salario = salario
# A:

funcionario1 = Funcionario("Jorge", 36, 1567)
print(funcionario1._salario)


# B: Não. O python nao impede o acesso.

# C: O objetivo do underline simples é proteger o atributo de ser alterado fora da classe.
