num = 0
pergunta = 0
media = 0
soma = 0
qtdnum = 0
maior = 0
menor = 0

while pergunta == 0:
    num = int(input('Digite os números inteiros: '))
    soma = num + soma
    qtdnum += 1
    media = soma/qtdnum
    if maior == 0 and menor == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    print('\nA média entre os números é {:.2f}'.format(media))
    print('O maior número digitado até o momento é {}'.format(maior))
    print('O menor número digitado até o momento é {}'.format(menor))
    pergunta = int(input('\nDeseja continuar a digitar valores? \n\n[0] Sim \n[1] Não\n\nDigite 0 ou 1: '))


print('\nFim do Programa!')