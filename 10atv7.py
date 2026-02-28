import os
def limpar():
    os.system("cls")
limpar()

class Produto:
 def __init__(self,nome, preco, quantidade):
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade 

 def valor_total(self):
    self.valor = self.preco * self.quantidade
    print(f"Produto: {self.nome}\nPreco: {self.preco:.2f}\nQuantidade: {self.quantidade}\nValor total: {self.valor:.2f}")

Produto1 = Produto("Linguiça de porco", 40, 13)
Produto1.valor_total()