print("_________ Seja bem-vindo Usuário _________")
resposta = int(input("Selecione abaixo em qual das medidas está a temperatura atual: \n 1- Celsius \n 2-Fahrenheit"))

def calcularCparaF():
    c = float(input("Selecione a temperatura em celsius agora:"))
    f = int
    f = (9 * c)/ 5 + 32
    print(f"A temperatura {c} celsius em fahrenheit é igual a {f}")
    
def calcularFparaC():
    f = float(input("Selecione a temperatura em Fahrenheit agora:"))
    c = int
    c = ((f - 32) * 5) / 9
    print(f"A temperatura {f} fahrenheit em celsius é igual a {c}")
    
    
if resposta == 1:
    calcularCparaF()
    
elif resposta == 2:
    calcularFparaC()
    
else :
    print("Resposta inválida!")