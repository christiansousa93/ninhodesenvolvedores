# Crie um algoritmo que receba 3 números e informe qual o maior entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2:
    print(f"{num1} é o número maior.")
elif num1 > num3:
    print(f"{num1} é o número maior.")
elif num2 > num1:
    print(f"{num2} é o número maior.")
elif num2 > num3:
    print(f"{num2} é o número maior.")
elif num3 > num1:
    print(f"{num3} é o número maior.")
elif num3 > num2:
    print(f"{num3} é o número maior.")
else:
    print("Os números são iguais.")
