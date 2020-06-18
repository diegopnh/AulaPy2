abr = input('Aperte enter para iniciar a soma.\n')

x = 0
for c in range(1,500):
    if c % 3 == 0 and c % 2 != 0:
        x = x + c
    else: 
        0
print('O resultado da soma foi {}'.format(x))