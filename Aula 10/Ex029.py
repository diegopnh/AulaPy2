vel = int(input('Qual foi a velocidade do carro?: '))
mul = (vel-80)*7

if vel > 80:
    print('Você passou o limite de 80km/h, por isso você será multado em R$ {:.2f}'.format(mul))
else:
    print('Você está dentro do limite de velocidade!')    
