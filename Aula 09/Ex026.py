a = str(input('Descreva sua frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase.'.format(a.count('A')))
print('A primeira letra A aparece na posição {}.'.format(a.find('A')+1))
print('A última letra A aparece na posição {}.'.format(a.rfind('A')+1))



