# Faça um algoritmo que leia dois números e indique se são iguais ou se são diferentes. Mostre o maior e o menor (nesta sequência).

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 == num2:
    print("Os números são iguais.")
if num1 != num2:
    print("Os número são diferentes.")
elif num1 > num2:
    print(f"{num1} é o número maior e o {num2} é o número menor.")
else:
    print(f"{num2} é o número maior e o {num1} é o número menor.")
