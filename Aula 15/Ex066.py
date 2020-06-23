number = count = sumNumber = 0

while True:
    if number == 999:
        break
    sumNumber = sumNumber + number
    number = int(input ('Escreva um número inteiro (999 para parar): '))
    count += 1

print(f'Foram digitados {count} números e a soma deles é {sumNumber}')