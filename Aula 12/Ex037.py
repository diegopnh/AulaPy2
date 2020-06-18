num = int(input('Escreva um número inteiro: '))
bas = int(input('Qual será a base de conversão?\n(1) Binário\n(2) Octal\n(3) Hexadecimal\n\nEscolha a opção: '))

if bas == 1:
    print('O número binário é {}'.format(bin(num)))
elif bas == 2:
    print('O número em octal é {}'.format(oct(num)))
elif bas == 3:
    print('O número em hexadecimal é {}'.format(hex(num)))
else: 
    print('Solicitação incorreta!')
