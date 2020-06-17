viag = int(input('Digite a distancia da viagem: '))

if viag > 200:
    print('O preço da passagem é de R$ {:.2f}!'.format(viag*0.45))
else:
    print('O preço da passagem é de R$ {:.2f}!'.format(viag*0.5))