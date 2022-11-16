nome = str (input ('Qual é o seu nome?: '))
nota1 = int (input ('Digite a primeira nota: '))
nota2 = int (input ('Digite a segunda nota: '))
nota3 = int (input ('Digite a terceira nota: '))
media = (nota1+nota2+nota3)/3

print (media)
    
if media>=7:
    print (nome,','' você foi aprovado')
elif (media<=5):
    print (nome,',' ' você foi reprovado')
else:
    print (nome,',' ' você está de recuperação')
