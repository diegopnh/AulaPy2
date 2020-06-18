a = 0
r = 0
a = int(input('Qual o primeiro termo da Progressão? '))
r = int(input('Qual a razão da Progressão? '))

print('A sequência da progressão é: ')
for c in range (1,11):
    print(a + (c-1)*r, end=' ')
  
    