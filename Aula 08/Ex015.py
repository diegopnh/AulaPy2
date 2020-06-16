k = float(input("Informe a quantade de km percorridos: "))
d = float(input("Informe a quantidade de dias que foi alugado: "))

t = (d*60) + (k*0.15)

print("\n","O preço a ser pago é de R$ {:.2f}".format(t))