nome = str(input('Escreva o nome completo: '))

print('Nome Maiusculo: {}'.format(nome.upper()))
print('Nome Minusculo: {}'.format(nome.lower()))
print('Tamanho do Nome: {}'.format(len(nome)-nome.count(' ')))
print('Primeiro Nome tem {} letras'.format(nome.find(' ')))