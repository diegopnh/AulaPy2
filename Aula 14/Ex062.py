a = int(input('Qual o primeiro termo da Progressão? '))
r = int(input('Qual a razão da Progressão? '))
c = 1
total = 0
mais = 10

print('A sequência da progressão é: ')

while mais != 0:
    total = total + mais
    while c <= total:
        print(a + (c-1)*r, end=' ')
        c += 1
    print('Pausado!')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))

print('Fim do Programa!')