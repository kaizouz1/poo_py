import os
def limpar():
    os.system("cls")
limpar()


class Produto:
 def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

 def mostrar_preco(self):
    print(f"O produto {self.nome} custa R${self.preco}")
produto1 = Produto("Coxinha que yuri deve", 14)
produto1.mostrar_preco()