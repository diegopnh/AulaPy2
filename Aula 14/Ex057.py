sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]

while sexo == 'M' or sexo == 'F':
    sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Valor incorreto. Digite novamente.')
        sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]