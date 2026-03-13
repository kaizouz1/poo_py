import os
def limpar():
    os.system("cls")
limpar()


class Estoque:
    def __init__(self,nome_produto, categoria, quantidade):
        self.nome_produto = nome_produto
        self._categoria = categoria
        self.__quantidade = 0

        if quantidade >= 0: 
         self.__quantidade = quantidade
        
    def consultar_quantidade(self):
        return (f"Quantidade: {self.__quantidade}")
    
    def alternar_quantidade(self, nova_quantidade):
       if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
            return (f"Nova quantidade: {nova_quantidade}")
       else:
         print("Quandantidade invalida!")

    
    def adicionar_produtos(self, quantidade, ):
       if quantidade > 0:
          self.__quantidade += quantidade
          return (f"Quantidade adicionada: {self.__quantidade}")
    
       else:
         return("Quantidade adicionada invalida.")

    def remover_quantidade(self, quantidade):
        if quantidade <= self.__quantidade and quantidade > 0:
            self.__quantidade -= quantidade
            return (f"Quantidade removida: {self.__quantidade}")
        else:
            print("Quantidade insuficiente no estoque ou valor inválido.")

produto1 = Estoque("Redmin 14C", "Smartphone", 10)     

print(produto1.consultar_quantidade())
print(produto1.alternar_quantidade(2))
print(produto1.adicionar_produtos(10))
print(produto1.remover_quantidade(14))


# Por que o atributo __quantidade foi definido como privado? 
# - porque o atributo quantidade é algo que não pode ser alterado por qualquer pessoa

# Qual a função do @property na classe? 
# - permite acessar o método como se fosse um atributo, mantendo a validação internamente

# Por que o método remover_estoque utiliza duas condições na verificação? 
# para verificar a quantidade anterior e a nova.

# O que aconteceria se a quantidade fosse um atributo público?
#  - Qualquer pessoa poderia alterna-la 

# Em um sistema real, quais riscos existiriam se não houvesse validação? 
# - Varias pessoas poderiam mudar os atributos, aumentando a quantidade de dinheiro em seus bancos, diminuindo o preço dos produtos etc.