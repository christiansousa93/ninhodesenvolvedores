#Crie uma função que determine se a letra escolhida existe na palavra

def checarletra (l, p):
    if (p.count(l)):
        print(f"A letra '{l}' existe na palavra '{p}'")
    else:
        print(f"A letra '{l}' não existe na palavra '{p}'")
    
checarletra1 = input ("Digite uma letra: ")
    
checarpalavra = input ("Digite uma palavra: ")
    
checarletra (checarletra1, checarpalavra)