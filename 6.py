#Lista de cardápio

c100 = str ('Cachorro quente')
pre100 = int (1.10)
c101 = str ('Bauru simples')
pre101 = int (1.30)
c102 = str ('Bauru c/ ovo')
pre102 = int (1.50)
c103 = str ('Hamburger')
pre103 = int (1.10)
c104 = str ('Cheeseburger')
pre104 = int (1.30)
c105 = str ('Refrigerante')
pre105 = int (1.00)



#Variáveis
produto = str (input ('Digite o código do produto: '))
qtde = int (input ('Digite a quantidade: '))

if c100:
    print (c100, 'R$', (qtde*pre100), ',00')
elif c101:
    print (c101, 'R$', (qtde*pre101), ',00')
elif c102:
    print (c102, 'R$', (qtde*pre102), ',00')
elif c103:
    print (c103, 'R$', (qtde*pre103), ',00')
elif c104:
    print (c104, 'R$', (qtde*pre104),',00')
elif c105:
    print (c105, 'R$', (qtde*pre105),',00')