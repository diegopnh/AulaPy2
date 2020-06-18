prec = float(input('Digite o preço do produto: '))
cond = int(input('Escolha a condição de pagamento: \n(1) A vista\n(2) A vista no cartão\n(3) 2x no cartão\n(4) 3x ou mais no cartão\n\nDigite o número da condição de pagamento: '))

if cond == 1:
    print('O produto terá 10% de desconto e custará {:.2f}'.format(prec*0.9))
elif cond == 2:
    print('O produto terá 5% de desconto e custará {:.2f}'.format(prec*0.95))
elif cond == 3:
    print('O produto manterá seu preço de {} e cada parcela será de {:.2f}'.format(prec,prec/2))
elif cond == 4:
    parc = float(input('Quantas parcelas? '))
    print('O produto terá juros de 20%, totalizando {:.2f}. Cada parcela será de {:.2f}'.format(prec*1.2,(prec*1.2)/parc))
else:
    print('Erro de Parametrização!')    