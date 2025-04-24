num = int(input('Escolha um numero a ser testado: '))

i = 2

while i < num:

    if num%i == 0:
        print(f'{num}/{i} = {num/i:.0f}')
        print('Numero não é primo')    
        break
        
    i += 1
else:
    print(f'{num} é um numero primo')
