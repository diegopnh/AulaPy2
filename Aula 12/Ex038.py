num1 = int(input('Escreva o primeiro valor: '))
num2 = int(input('Escreva o segundo valor: '))

if num1 > num2:
    print('{} é maior do que {}'.format(num1,num2))
elif num2 > num1:
    print('{} é maior do que {}'.format(num2,num1))
else:
    print('Não existe valor maior, os números são iguais.')
