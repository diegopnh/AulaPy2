from random import choice
a = input(str('Digite o primeiro aluno: '))
b = input(str('Digite o segundo aluno: '))
c = input(str('Digite o terceiro aluno: '))
d = input(str('Digite o quarto aluno: '))
lista = [a,b,c,d]
x = choice(lista)
print('O escolhido para limpar o quadro é: {}'.format(x))