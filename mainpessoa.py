import os
def limpar():
    os.system("cls")
limpar()

from aleatorio import Pessoa, Aluno, Professor

a = Aluno("Kaizou", 20)
p = Professor("Ana", 35)

p.apresentar()
p.ensinar()


a.apresentar()
a.estudar()
