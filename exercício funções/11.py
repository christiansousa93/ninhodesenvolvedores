#Faça uma função que computa a potência a^b para valores a e b (assuma números inteiros) passados por parãmetros 
# (não use o operador **)

base = int(input("Digite a base: ")) # base a
expoente = int(input("Digite o expoente: ")) # expoente b
resultado = 1
for numero in range(1,expoente+1):
# base ** expoente = base * base (expoente vezes)

    resultado = resultado * base
print(base, "elevado a", expoente, "=", resultado)

def potencia(base,expoente):
 if expoente >= 0 :
    resultado = 1
    for numero in range(expoente):
        resultado = resultado * base
    return resultado
 else:
    resultado = 1
    for numero in range(-expoente):
        resultado = resultado / base
    return resultado
