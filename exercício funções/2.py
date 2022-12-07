#Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom,
#considerando 10% do valor da conta.

def calculargorjeta():
    valordaconta = input("Escreva o valor da conta: ")
    print (f"O valor da gorjeta é: R$", float(valordaconta)*0.1)
    
calculargorjeta()    
    