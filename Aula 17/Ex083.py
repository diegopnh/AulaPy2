aberto = 0
fechado = 0

expressao = str(input('Digite a expressão: '))
separado = list(expressao)

for c in range(0,len(separado)):
    if separado[c] == '(':
        aberto += 1
    elif separado[c] == ')':
        fechado += 1
    else:
        pass

if aberto == fechado: 
    print('A formula foi fechada corretamente!')
else:
    print('A formula foi fechada incorretamente!')