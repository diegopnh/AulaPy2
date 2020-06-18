print('Digite o peso das 5 pessoas \n')
maor = 0
menr = 0

for c in range (0,5):
    peso = float(input('Peso:'))
    if maor == 0:
        maor = peso
    elif menr == 0:
        menr = peso
    elif peso > maor:
        maor = peso
    elif peso < menr:
        menr = peso
    else:
        pass

print('O maior peso é de {:.2f}kg e o menor peso é {:.2f}kg'.format(maor,menr))
 