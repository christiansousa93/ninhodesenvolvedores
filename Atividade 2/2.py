# Ler um ano de nascimento e ano atual. Imprimir a idade da pessoa.
# Se a idade for maior ou igual a 18 leia o nome da pessoa e imprima o nome digitado e uma mensagem informando que sua entrada é permitida.
# (Ex: Fulano, sua entrada foi permitida.)

nome = str(input("Digite seu nome: "))
ano = int(input("Digite seu ano de nascimento: "))
anoatu = int(2022)
idade = (anoatu-ano)
print(f"{nome}, você tem {idade} anos")


if idade >= 18:
    print(f"{nome}, sua entrada está permitida no estabelecimento.")
else:
    print(f"{nome}, entrada não permitida.")
