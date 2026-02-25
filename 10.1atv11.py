import os
def limpar():
    os.system("cls")
limpar()


class Celular:
 def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

 def desc(self):
    print(f"Celular marca {self.marca} modelo {self.modelo}")
celular1 = Celular("Nokia", "Tijolão")
celular1.desc()