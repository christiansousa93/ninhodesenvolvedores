#Crie um programa que utilize uma função para comparar o tamanho de 2 palavras.
#Essa função vai receber as 2 palavras e vai determinar qual das duas palavras é a maior e imprimir na tela.

def maiorpalavra(pal1, pal2):
    if (len(pal1) > len(pal2)):
        print (f"A palavra {pal1} tem mais caracteres que {pal2}")
    elif (len(pal1) < len(pal2)):
        print (f"A palavra {pal2} tem mais caracteres que {pal1}")
    elif (len(pal1) == len(pal2)):
        print (f"A palavra {pal1} tem o mesmo número de caracteres que {pal2}")
    else:
        print("Algo deu errado")

while (True):   
    palavra1 = input ("Insira uma palavra: ")
    palavra2 = input ("Insira outra palavra: ")

    maiorpalavra (palavra1, palavra2)


        

