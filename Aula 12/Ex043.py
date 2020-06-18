peso = float(input('Digite o seu peso: '))
altr = float(input('Digite a sua altura: '))

imc = peso/(altr**2)

if imc < 18.5:
    print('Essa pessoa está abaixo do peso. O IMC é {:.2f}'.format(imc))
elif  18.5 <= imc < 25:
    print('Essa pessoa está no peso ideal. O IMC é {:.2f}'.format(imc))
elif 25 <= imc < 30:
    print('Essa pessoa está em Sobrepeso. O IMC é {:.2f}'.format(imc))    
elif 30 <= imc < 40:
    print('Essa pessoa está obesa. O IMC é {:.2f}'.format(imc))
elif imc >= 40:
    print('Essa pessoa está em Obesidade Morbida. O IMC é {:.2f}'.format(imc) )
else:
    print('Erro de Parâmetros!')

