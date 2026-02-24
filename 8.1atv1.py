import os
def limpar():
    os.system("cls")
limpar()

class Produto:
    
 def init(self, nome, preco):

  self.nome = nome

  self.preco = preco

 def exibir_informacoes(self): 
    print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}")

produto1 = Produto("Notebook", 3500.00)
produto1.exibir_informacoes()