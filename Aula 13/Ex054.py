from datetime import date
x = date.today().year
mnr = 0
mai = 0

print('Insira o ano das sete pessoas correspondentes')
for c in range(1,8):
    ano = int(input('Digite o ano que a {}º pessoa de nascimento da pessoa: '.format(c)))
    ida = x - ano
    if ida < 21:
        mnr = mnr + 1
    else:
        mai = mai + 1

print('\n O número de pessoas maior de idade é {} e menor de idade é {}.'.format(mai,mnr))