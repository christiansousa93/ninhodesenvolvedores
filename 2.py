anonasc = float (input ('Digite seu ano de nascimento: '))
anoatual = int (2022)
idade = int (anoatual-anonasc)
nome = (input ('Digite seu nome: '))

print ('A sua idade é: ', idade, ' anos') 


if idade >=18:
    print (nome,', sua entrada foi permitida')
elif idade <=18:
    print (nome,', entrada proibida')