import os
def limpar():
    os.system("cls")
limpar()


class Retangulo:
 def __init__(self, base, altura):
    self.altura = altura
    self.base = base

 def calculo_area(self):
    return self.base * self.altura
ret = Retangulo(5,6)
print(f"Área do retângulo: {ret.calculo_area()}")