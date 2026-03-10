import os 
def limpar():
    os.system("cls")
limpar()

senha = print(input("digite a senha: "))

if senha != "1234":
    print("Acesso concedido!")
else:
    print("Acesso negado!")