import os 
def limpar():
 os.system("cls")
limpar()

print("=== Produtos ===\n")

print("Produto 1:")
class Item:
  
 def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco 
 
 def informacao(self):
  print(f"Item: {self.nome}, Preço: R${self.preco:.2f}")

produto1 = Item("Lapis", 1.50)
produto1.informacao()


print("\nProduto 2:")
class Caderno:
   
 def __init__(self, folhas, preco, materias, capa):
    self.folhas = folhas
    self.materias = materias
    self.capa = capa
    self.preco = preco
  
 def info(self):
    print(f"folha: {self.folhas}")
    print(f"matérias: {self.materias}")
    print(f"capa: {self.capa}")
    print(f"preço: {self.preco:.2f}")

produto2 = Caderno(400, 20, "Capa Dura", 45.90)
produto2.info()
