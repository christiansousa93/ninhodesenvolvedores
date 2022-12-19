# Faça um algoritmo que leia dois números nas variáveis NumA e NumB, nessa ordem, e imprima em ordem inversa, isto é, se os dados lidos forem NumA = 5 e NumB = 9, por exemplo,
# devem ser impressos na ordem NumA = 9 e NumB = 5.

numa = int(input("Digite um número: "))
numb = int(input("Digite outro número: "))

inverso = int(str(numa, numb)[::-1])
print(inverso)
