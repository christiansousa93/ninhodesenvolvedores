# Ler 1 número. Se positivo, imprimir raiz quadrada senão o quadrado do número.

num = int(input("Digite um número: "))

if (num >= 0):
    print(num ** (1/2))
elif (num >= 0):
    print(num * 4)
else:
    print("Número incorreto.")
