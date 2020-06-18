from datetime import datetime
hoje = datetime.today().year

nasc = int(input('Informe o ano de nascimento do nadador: '))
idad = hoje - nasc

if idad > 20:
    print('O nadador é da categoria MASTER!')
elif idad < 19 and idad >= 14:
    print('O nadador é da categoria SÊNIOR!')
elif idad < 14 and idad >= 10:
    print('O nadador é da categoria INFANTIL!')
else:
    print('O nadador é da categoria MIRIM!')