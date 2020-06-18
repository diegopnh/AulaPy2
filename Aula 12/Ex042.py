a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if a < b + c and b < a + c and c < b + a:
    print('O triangulo pode ser formado!',end='')
    if a == b == c:
        print(' E é um triangulo Equilatero!')
    elif a != b != c !=a:
        print(' E é um triangulo Escaleno!')
    else:
        print('E é um triangulo Isóceles')
else:
    print('O triangulo não pode ser formado!')