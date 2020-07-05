palavras = ('aprender','programar','linguagem','python','curso',
            'curso', 'gratis','estudar','praticar','trabalhar','mercado',
            'programador', 'futuro')
vogais = ('a','e','i','o','u')

for x in range(0,len(palavras)):
    tamanho = len(palavras[x])
    print(f'\nAs vogais da palavra {(palavras[x])} são:',end=" ")
    for y in range(0,tamanho):
        letra = palavras[x][y]
        for z in vogais:
            if z == letra:
                print(letra,end=" ")
            elif y == tamanho: 
                break