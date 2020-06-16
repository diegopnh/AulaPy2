from random import shuffle
a = str(input('Digite o primeiro aluno: '))
b = str(input('Digite o segundo aluno: '))
c = str(input('Digite o terceiro aluno: '))
d = str(input('Digite o quarto aluno: '))
lista = [a,b,c,d]
shuffle(lista)
print('A ordem de apresentação do trabalho é: ')
print(lista)