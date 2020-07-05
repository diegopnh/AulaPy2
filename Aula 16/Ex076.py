print(40*'-')
print('LISTAGEM DE PREÇOS')
print(40*'-')

produtos = ('Lápis','1.75',
            'Borracha', '2',
            'Caderno','15.9',
            'Estojo','25',
            'Transferidor','4.2',
            'Compasso','9.99',
            'Mochila','120.32',
            'Canetas','22.3',
            'Livro','34.9')

fim = len(produtos)
for x in range(0,fim):
    if x % 2 == 0:
        print(f'{produtos[x]:.<30}', end="")
    else:
        print(f'R${float(produtos[x]):>7.2f}')
    