salario = float (input ('Qual é o seu salário: '))
prestacao = float (input ('Qual o valor da prestação: '))
salario20 = int (salario)*0.2

if (prestacao > salario20)/0.8:
    print ('Empréstimo não pode ser concedido.')
elif (prestacao <= salario20)/0.8:
    print ('Empréstimo pode ser concedido.')