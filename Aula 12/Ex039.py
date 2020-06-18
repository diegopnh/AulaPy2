from datetime import datetime
ano = datetime.today().year
nasc = int(input('Informe a data de nascimento: '))
idad = ano - nasc

if idad == 18:
    print('É hora de se alistar!')
elif idad < 18:
    print('Ainda é muito cedo! Faltam {} ano(s) para ele(a) se alistar!'.format(18-idad))
else:
    print('Já passou do prazo de alistamento!')