a = int(input('Qual o primeiro termo da Progressão? '))
r = int(input('Qual a razão da Progressão? '))
c = 1

print('A sequência da progressão é: ')
while c <= 10:
    print(a + (c-1)*r, end=' ')
    c += 1