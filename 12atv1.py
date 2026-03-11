import os 
def limpar():
    os.system("cls")
limpar()


class Pessoa: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self._idade = idade 
        self.__cpf = "123.456.789-00"
    


# Responda: 

# a) Qual atributo é público? 
# - O atributo nome.

# b) Qual é protegido?
# # - O atributo idade. 

# c) Qual é privado? 
# - O atributo cpf

# d) Qual deles pode ser acessado diretamente sem erro?
# O atributo nome. 


