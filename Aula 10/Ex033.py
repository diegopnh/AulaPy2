a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))

menor = a
if b<a and b>c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))