not1 = float(input('Escreva a primeira nota do aluno: '))
not2 = float(input('Escreva a segunda nota do aluno: '))

meda = (not1 + not2)/2

if meda < 5.0:
    print('O aluno foi reprovado! Sua média foi {:.2f}!'.format(meda))
elif meda >= 5.0 and meda < 7.0:
    print('O aluno ficou em recuperação! Sua média foi {:.2f}'.format(meda))
else:
    print('O aluno foi aprovado com a média {:.2f}'.format(meda))