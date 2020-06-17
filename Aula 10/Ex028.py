from random import randrange
pc = randrange(5)

user = int(input('Descubra o número de 0 a 5 que está na memória do PC: '))
if user == pc:
    print('O número que o computador pensou foi {}, ou seja, você está certo!'.format(pc))
else:
    print('O número que o computador pensou foi {}, ou seja, você está errado!'.format(pc))
