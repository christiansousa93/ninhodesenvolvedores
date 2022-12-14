#2. Classe Funcionário: Implemente a classe Funcionário. Um funcionário tem um  nome e um salário.
# Escreva um construtor com dois parâmetros (nome e salário) e o método aumentarSalario (porcentualDeAumento)
# que aumente o salário do funcionário em uma certa porcentagem. Exemplo de uso: 
#harry = funcionario( " Harry" , 25000 ) 
#harry.aumentarSalario(10) 
#Faca um programa que teste o método da classe.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def aumentarSalario(self, porcentualDeAumento):
        self.salario = self.salario * (1+(porcentualDeAumento/100))
        
funcionario1 = Funcionario("José", 30000)

print (f"Salário atual: {funcionario1.salario}")

funcionario1.aumentarSalario(20)

print   (f"Salário depois do aumento: {funcionario1.salario}")