print('Mini Calculadora')

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
result = 0
option = 0

while option != 5:
    option = float(input("""Veja as opções em relação aos valores:

[1] Somar
[2] Multiplicar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa

Insira o valor aqui: """))

    if option == 1:
        result = a + b
        print(result)
    elif option == 2:
        result = a*b
        print(result)
    elif option == 3:
        if a > b:
            print('O número {} é maior do que {}.'.format(a,b))
        else:
            print('O número {} é maior do que {}.'.format(b,a))
    elif option == 4:
        a = float(input('Insira novo primeiro número:'))
        b = float(input('Insira novo segundo número: '))

print('Você saiu do programa!')