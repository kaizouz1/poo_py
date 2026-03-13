import os 
def limpar():
    os.system("cls")
limpar()


class Aluno:
    def __init__(self, nota=0):
        self.nota = nota  

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, valor):
        if 0 < valor < 10:
            self.__nota = valor
        else:
            print("Erro: a nota deve estar entre 0 e 10.")


aluno1 = Aluno(8)     
print(aluno1.nota)

aluno1.nota = 9     
print(aluno1.nota)

aluno1.nota = 11    
print(aluno1.nota)

aluno1.nota = -3    
print(aluno1.nota)

