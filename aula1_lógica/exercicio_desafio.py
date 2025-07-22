import random
numero_doprograma = random.randint(1, 100)  # Gera um inteiro entre 1 e 100

def jogo():
    tentativas = 1
    numero_jogador = int(input("Selecione o número para tentar acertar:\n"))
    while numero_jogador != numero_doprograma:
        if numero_jogador < numero_doprograma:
            print("O número é menor que o da máquina!\n")
        else:
            print("O número é maior que o da máquina!\n")
        numero_jogador = int(input("Selecione o número para tentar acertar: \n"))
        tentativas += 1
        
    print(f"Parabéns você acertou o número com {tentativas} tentativas! ")   
    
    
print("______ Bem-vindo ao jogo da sorte ______\n")
print("Tente adivinhar o número entre 1 a 100\n")
jogo()
