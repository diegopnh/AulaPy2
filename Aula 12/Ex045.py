from random import randint
itens = ('Pedra','Papel','Tesoura')
comp = randint (0,2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
user = int(input('Qual a sua jogada? '))
print('Computador jogou {}'.format(itens[comp]))
print('Jogador jogou {} \n'.format(itens[user]))

if comp == 0:
    if user == 0:
        print('Empatou!')
    elif user == 1:
        print('Jogador Vence!')
    elif user == 2:
        print('Jogador Perde!')
    else:
        print("Erro de Parâmetro!")
elif comp == 1:
    if user == 0:
        print('Jogador Perde!')
    elif user == 1:
        print('Empatou!')
    elif user == 2:
        print('Jogador Vence!')
    else:
        print("Erro de Parâmetro!")
elif comp == 2:
    if user == 0:
        print('Jogador Vence!')
    elif user == 1:
        print('Jogador Perde!')
    elif user == 2:
        print('Empatou!')
    else:
        print("Erro de Parâmetro!")