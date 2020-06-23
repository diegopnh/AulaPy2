print(20*'-','Cadastro de Produtos','-'*20)

product = str(input('Nome do Produto: '))
price = float(input('Preço do produto: R$ '))
sumPrice = qtdProduct = cheapProduct = 0

while True:
    contn = str(input('Quer continuar? [Y/N]: ')).upper()
    sumPrice = sumPrice + price
    if price > 1000:
        qtdProduct += 1
    if price < cheapPrice or cheapProduct = 0:
        cheapPrice = price
        cheapProduct = product   
    if contn == "Y":
        product = str(input('Nome do Produto: '))
        price = float(input('Preço do produto: R$ '))
    if contn == "N":
        break

print(f'O total de compra foi {sumPrice:.2f}')
print(f'Temos {qtdProduct} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi a/o {cheapProduct} que custa R$ {cheapPrice:.2f}')