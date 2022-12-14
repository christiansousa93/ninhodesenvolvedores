#Crie uma classe chamada Pokemon. Tente imaginar os atributos que um objeto dessa classe teria.
#Faça um programa que instância um objeto da classe Pokemon e imprima os atributos desse objeto.
#Bônus: Crie 2 objetos Pokemon e tente criar uma função de batalha que recebe os 2 objetos e determine quem sai ganhando.

class Pokemon:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder
        
if __name__ == "__main__":
    pikachu = Pokemon("Pikachu", "300")
    print(f"O Pokemon {pikachu.nome} tem {pikachu.poder} de poder")
        
if __name__ == "__main__":
    squirtle = Pokemon("Squirtle", "400")
    print(f"O Pokemon {squirtle.nome} tem {squirtle.poder} de poder")

if (pikachu.poder < squirtle.poder):
   print(f"{squirtle.nome} venceu")
elif (pikachu.poder > squirtle.poder):
   print(f"{pikachu.nome} venceu")
else:
    print("Empate")
    
