resposta = 0

def contador():
    resposta = int(input("Digite a seguir um número para ser iniciado a contagem: "))
    for i in range (1,resposta+1):
         print(f" {i} ")

print("_____ Bem-vindo ao contador _____")
contador()
