import os 
def limpar():
    os.system("cls")
limpar()



class Animal:
    def fala(self):
     print("O cachorro late")
class Cachorro(Animal):
    def falar(self):
     print("Auau")

dog = Cachorro()
dog.fala()
dog.falar()