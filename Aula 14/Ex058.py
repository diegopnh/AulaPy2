from random import randrange
pc = randrange(11)
tentativas = 0
user = int(input('Descubra o número de 0 a 10 que está na memória do PC: '))

while user != pc:
    tentativas = tentativas + 1
    user = int(input('Tente novamente: '))
    if pc == user:
        print('O número do PC era {} e você precisou de {} tentativas para isso.'.format(pc,tentativas))