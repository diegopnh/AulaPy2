from math import hypot 
a = float(input('Digite o cateto oposto: '))
b = float(input('Digite o cateto adjacente: '))
h = hypot(a,b)

print('A hipotenusa é: {:.2f}'.format(h))