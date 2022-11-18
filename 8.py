#Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.

repetir = 10
contador = 0

for i in range(repetir):
    n = int (input(f"Escreva o número {i+1}: "))
    if (n>=10 and n <=50):
        contador += 1
print("A quantidade de números foi: ",contador)