num = int(input('Escolha um numero a ser testado: '))

i = 2

while i < num:

    if num%i == 0:
        print(num,'/',i, ' = ', num/i)
        print('Numero não é primo')    
        break

    i += 1

else:
    print(num, 'é um numero primo')
