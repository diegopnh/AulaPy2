frase = str(input('Digite uma frase qualquer: ').strip())

fraseSemEspaco = frase.replace(' ', '').upper()

for c in range(1):
    if fraseSemEspaco[len(frase)::-1] == fraseSemEspaco[0:len(frase)+1]:
        print('É um PPALÍNDROMO')
    else:
        print('NÃO É UM PALÍNDROMO!')

