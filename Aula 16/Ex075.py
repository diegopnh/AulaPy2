numeros = (int(input('Digite o primeiro valor: ')),
        int(input('Digite o segundo valor: ')),
        int(input('Digite o terceiro valor: ')),
        int(input('Digite o quarto valor: ')))

print(f'A lista de números digitados foi {numeros}')
print(f'O número 9 aparece {numeros.count(9)} vezes na lista')

if 3 in numeros:
    print(f'A primeira vez que apareceu um 3 foi na {numeros.index(3)+1}º posição.')
else:
    print(f'Não existe o algarismo 3 na lista.')

print('Os valores pares digitados foram:',end=" ")
for y in numeros:
    if y % 2 == 0:
        print(y, end=" ")