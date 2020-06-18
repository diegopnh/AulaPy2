a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if a < b + c and b < a + c and c < b + a:
    print('O triangulo pode ser formado!')
else:
    print('O triangulo não pode ser formado!')