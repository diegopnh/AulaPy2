sal = float(input('Qual é o salário do funcionário?: '))

if sal > 1250:
    print('O aumento do salário deverá ser de R$ {:.2f}, totalizando R$ {:.2f}'.format(sal*0.1,sal*1.1))
else:
    print('O aumento do salário deverá ser de R$ {:.2f}, totalizando R$ {:.2f}'.format(sal*0.15,sal*1.15))
    