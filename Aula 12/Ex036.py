casa = float(input('Escreva o valor da casa: '))
salr = float(input('Escreva o salário mensal do comprador: '))
anos = float(input('Quantos anos ele quer pagar?: '))

mess = anos*12
pret = casa/mess
parc = pret/salr

if parc > 0.3:
    print('O emprestimo deve ser negado porquê o valor da parcela excedeu 30%. \nParcela em relação ao salário: {0:.2%}'.format(parc))
else:
    print('O emprestimo pode ser aceito. \nParcela em relação ao salário: {0:.2%}'.format(parc))
