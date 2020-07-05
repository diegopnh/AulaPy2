extenso = ('Zero', 'Um','Dois','Três','Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
            'Quinze', 'Dezesseis','Dezessete','Dezoito',
            'Dezenove', 'Vinte')

numero = int(input('Digite um número entre 0 e 20: '))
while 0 < numero < 20:
    numero = int(input('Tente Novamente. Digite um número entre 0 e 20: '))

print(f'O número por extenso é {extenso[numero]}')



