from random import randint
player = int(input('Digite um valor: '))      
game = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
sumGame = 0
count = 0

while True:
    pc = randint(1,10)
    sumGame = player + pc
    if sumGame % 2 == 0:
        gamePrint = "PAR"
        gameTotal = "P"
    else:
        gamePrint = "IMPAR"
        gameTotal = "I"
    print(f'\nVocê jogou {player} e o computador {pc}. Total de {sumGame} deu {gamePrint}')
    if game == gameTotal:
        count += 1
        print('Você venceu!\nVamos jogar novamente?\n')
        player = int(input('Digite um valor: '))
        game = str(input('Par ou impar? [P/I]: ')).upper().strip()[0]
    else:
        print(f'Você perdeu!\nGAME OVER! Você venceu {count} vezes.')
        break