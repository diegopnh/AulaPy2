number = int(input('Qual a tabuáda que você deseja?: '))
count = 0

while True: 
    if number <= 0:
        break
    elif count >= 10:
        count = 0
        number = int(input('\nQual a tabuáda que você deseja?: '))
    else:
        count += 1
        print(f'{number} x {count} = {number*count}')

print('Fim do Programa!')

