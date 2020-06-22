a = int(input('Insira o fatorial: '))
result = 1
n = 1

while n <= a:
    result = result*n
    n = n + 1

print('O fatorial de {} é {}'.format(a,result))