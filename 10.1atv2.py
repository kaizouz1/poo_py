import os 
def limpar():
    os.system("cls")
limpar()

class Pessoa:
    def __init__(self, nome, idade, cidade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.cidade = cidade
    
    def apresentar(self):
        print(f"eu me chamo {self.nome} e tenho {self.idade} anos. Sou um {self.profissao} e moro na cidade de {self.cidade}")

    def aniversario(self):
        self.idade += 1

    def mensagem2(self):
        print(f"eu me chamo {self.nome} e tenho {self.idade} anos. Sou um {self.profissao} e moro na cidade de {self.cidade}")



pessoa1 = Pessoa("Carlos", 25, "Vitoria", "programador" )
pessoa1.apresentar()
print("===" * 20)
pessoa1.aniversario()
pessoa1.mensagem2()0998
