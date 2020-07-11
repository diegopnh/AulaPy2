valores = list()
pert = 0
pert = "S"
count = 0

while pert == "S":
    num = int(input('Digite um valor: '))
    pert = str(input('Deseja continuar? [S/N]: ')).upper()
    valores.append(num)
    count += 1

valores.sort(reverse=True)

print(f'Você digitou {count} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'A lista possuí o número 5.')
else:
    print(f'A lista não possuí o número 5.')
