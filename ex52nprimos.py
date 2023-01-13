numero = int(input('Digite um numero: '))
tot = 0
for cont in range (1, numero +1):
    if numero % cont == 0:
        print('\033[34m', end= ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print('{} '.format(cont), end= ' ')

print('\n\033[mO número {} foi divisivel {} vezes.'.format(numero, tot))

if tot == 2:
    print('O numero {} é divisivel por si e por 1, por isso é primo'.format(numero))
else:
    print('O número {} não é primo'.format(numero))