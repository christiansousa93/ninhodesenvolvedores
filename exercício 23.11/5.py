def calcular_pagamento(qtde_horas, valor_hora):
    horas = float (qtde_horas)
    taxa = float (valor_hora)
    if horas <= 40:
        salario=horas * taxa
    else:
        h_excd = horas - 40
        salario = 40*taxa+(h_excd*(1.5*taxa))     
    return salario

horastrabalhadas = input("Quantas horas você trabalhou? ")
valordahora = input ("Quanto custa a sua hora? ")

salariorecebido = calcular_pagamento(40, 15)

print(f"Você recebeu R$", salariorecebido, "e trabalhou", horastrabalhadas, "horas semanais")