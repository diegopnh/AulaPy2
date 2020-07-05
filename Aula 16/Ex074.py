from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'A lista de números é {numeros}')

novatupla = sorted(numeros)
print(f'O menor número é {novatupla[0]}')
print(f'O maior número é {novatupla[-1]}')


