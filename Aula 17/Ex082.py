todos = list()
pergt = 'S'

while pergt == 'S':
    num = int(input('Digite aqui um número: '))
    todos.append(num)
    pergt = str(input('Deseja continuar? [S/N]: ')).upper()

pares = list()
impares = list()

for count in todos:
    if todos[count] % 2 == 0 or todos[count] == 0:
        x = todos[count]
        pares.append(x)
    else:
        y = todos[count]
        impares.append(y)

print(f'Os números digitados foram {todos}')
print(f'Os números pares são {pares}')
print(f'Os números impares são {impares}')



