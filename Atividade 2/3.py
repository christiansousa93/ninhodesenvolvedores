# Solicitar salário, prestação. Se prestação for maior que 20% do salário, imprimir : Empréstimo não pode ser concedido.
# Senão imprimir Empréstimo pode ser concedido.

salario = int(input("Digite seu salário: "))
prestacao = int(input("Digite o valor da sua prestação: "))

if prestacao <= 20 % salario:
    print("Empréstimo pode ser concebido.")
elif prestacao >= 21 % salario:
    print("Empréstimo não pode ser concebido.")
