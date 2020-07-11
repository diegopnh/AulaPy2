sequencia = list()
i = 0

for i in range(0,5):
    valor = int(input('Digite o valor: '))
    if i == 0:
        sequencia.insert(i,valor)
        print(f'Inserido o primeiro número da lista')
    else:
        j = 0
        while valor > sequencia[0+j]:
            j += 1
            if j == i:
                break
        sequencia.insert(j,valor)
        print(f'Inserido o valor {valor} na posição {j}')

print(f'A sequência de valores é {sequencia}')