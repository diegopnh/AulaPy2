nome = str(input('Qual é o seu nome? ')).strip()
a = nome.find(' ')
b = nome.rfind(' ')
print('o seu primeiro nome é: {}'.format(nome[:a]))
print('o seu último nome é: {}'.format(nome[b+1:]))