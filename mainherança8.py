import os 
def limpar():
    os.system("cls")
limpar()


from herança8 import Personagem, Guerreiro, Mago



guerreiro1 = Guerreiro("Kaizouz1")
print(guerreiro1.atacar())


mago1 = Mago("Rafaelsantt")
print(mago1.atacar())