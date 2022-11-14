numero1= int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2:
    if numero2 > numero3:

       print(f'{numero1} é o maior.')

elif numero2 > numero3:

   if numero3 > numero1:

       print(f'{numero2} é o maior.')

else:

   print(f'{numero3} é o maior.')


