from datetime import date
ano = int(input('Digite o ano: '))
quc = ano % 400
cem = ano % 100
quu = ano % 4

if ano == 0:
    ano = date.today().year
if quc == 0 and cem != 0 or quu == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))