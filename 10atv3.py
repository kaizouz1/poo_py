import os 
def limpar():
    os.system("cls")
limpar()


class Produto:
 def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco
    self.preco_original = preco

 def aplicar_desconto(self,percentual):
    desconto = (self.preco * percentual / 100)
    self.preco -= desconto
 
 def mostrar(self):
    print(f"Nome: {self.nome}\nPreço original: {self.preco_original:.2f}")
    print(f"Preço com desconto: {self.preco:.2f}")

produto1 = Produto("SSD 1TB", 2500)
produto1.aplicar_desconto(15)
produto1.mostrar()