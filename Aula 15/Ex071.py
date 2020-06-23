print('='*20,' CAIXA ELETRÔNICO ','='*20,'\n')

money = int(input('Digite o valor que deseja sacar: '))
fifty = twenty = ten = one = 0

while True:
    if money == 0:
        break
    if money >= 50:
        fifty += 1
        money = money - 50
    elif money >= 20:
        twenty += 1
        money = money - 20
    elif money >= 10:
        ten += 1
        money = money - 10
    elif money < 10:
        one += 1
        money = money - 1
        
print(f'Você receberá {fifty} notas de R$50')
print(f'Você receberá {twenty} notas de R$20')
print(f'Você receberá {ten} notas de R$10')
print(f'Você receberá {one} notas de R$1')

print('\nVolte Sempre!')
