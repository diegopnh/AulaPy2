valores = list()

for posicao in (range(0,5)):
    valores.append(int(input(f'Digite um valor para a posição {posicao}: ')))

maior = max(valores)
menor = min(valores)

print(f'Você digitou os valores {valores}')

print(f'O maior valor da lista é {maior} e estão na posição: ', end="")
for x, i in enumerate(valores):
    if i == maior:
        print(x, end=" ")
    x += 1

print(f'\nO menor valor da lista é {menor} e estão na posição: ', end="")
for y, i in enumerate(valores):
    if i == menor:
        print(y, end=" ")
    y += 1