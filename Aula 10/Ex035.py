a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if a < b + c or b < a + c or c < b + a:
    print('O triangulo pode ser formado!')
else:
    print('O triangulo não pode ser formado!')
