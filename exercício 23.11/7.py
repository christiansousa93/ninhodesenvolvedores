def soma(numero1, numero2):
    return float(numero1) + float(numero2)
def subtracao(numero1, numero2):
    return float(numero1) - float(numero2)
def multiplicacao(numero1, numero2):
    return float(numero1) * float(numero2)
def divisao(numero1, numero2):
    return float(numero1) / float(numero2)

num1 = input("Escreve o número 1: ")
num2 = input("Escreve o número 2: ")
operador = input("Escreva o operador (+,-,*,/)")

if (operador == "+"):
    print (f"A soma dos números é: ", soma(num1, num2))
elif (operador == "-"):
    print (f"A subtração dos números é: ", subtracao(num1, num2))
elif (operador == "*"):
    print (f"A multiplicação dos números é: ", multiplicacao(num1, num2))
elif (operador == "/"):
    print (f"A divisão dos números é: ", divisao(num1, num2))
else:
    print("Dados inválidos")