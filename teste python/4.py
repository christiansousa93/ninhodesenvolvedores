a = int (input('Digite um número: '))
b = int (input('Digite um número: '))
c = int (input('Digite um número: '))

if (a!=b!=c):
    numbers= [a,b,c]
    numbers.sort(reverse=True)
    print(numbers)
if (a==b==c):
    print('Os números não podem se repetirem')
    



