print('Digite números inteiros. Se os números forem par, o script fará a soma desses números. \n')

a = 0
for c in range (0,6):
    b = int(input('Digite um número: '))
    if b % 2 == 0:
        a = a + b
    else:
        pass

print('O resultado da soma é {}'.format(a))


