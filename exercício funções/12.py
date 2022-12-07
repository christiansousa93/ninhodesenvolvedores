#Escreva um programa que recebe um número inteiro e use uma função para determinar se é um número inteiro ou não,
#se o texto inserido não for um número inteiro, peça para o usuário digitar novamente.
#Dicas: isnumeric() repetir = True while(repetir) 

def inteiro (n):
    if (n.isnumeric()):
        print (f"O número ",n," é um número inteiro")
        global repetir
        repetir = False
    else:
        print (f"O número ",n, " não é um número inteiro")
        print ("Digite novamente")

repetir = True

while (repetir):
    num = input ("Digite um número inteiro: ")
    inteiro (num)
    
    
####Outra alternativa

while (True):
    num = input ("Digite um número inteiro: ")
    
    if (num.isnumeric()):
        print (f"O número ",num," é um número inteiro")
        break
    else:
        print("O número ",num," não é um numero inteiro")