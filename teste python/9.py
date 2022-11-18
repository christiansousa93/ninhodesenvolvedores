

largura = int (input("Digite a largura: "))
altura = int (input("Digite a altura: "))

linha = ""

for l in range (largura):
    linha += "# "

for a in range (altura):
    print(linha)
    