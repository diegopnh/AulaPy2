#Váriaveis
idade = 0 # Média de idade
maisvelho = 0 # idade Mais Velho
nomevelho = 0 # Nome do Mais Velho
qtmulher = 0 # Quantidade de Mulheres

#Formulário de Informações
for c in range(0,4):
    nofr = str(input('\nDigite o nome da Pessoa: '))
    idfr = int(input('Digite a idade da Pessoa: '))
    sefr = str(input('Digite o sexo da pessoa: ')).upper()
    idade = idade + idfr
    if idfr > maisvelho and sefr == "M": # Nome do Homem Mais Velho
        maisvelho = idfr
        nomevelho = nofr
    else:
        pass
    if sefr == "F" and idfr < 20: # Quantidade de Mulheres
        qtmulher = qtmulher + 1
    else:
        pass

#Print
print('\n A média de idade das 4 pessoas é de {:.2f} anos.'.format(idade/4)) #Calculo de Média de Idade
print('O nome do homem mais velho é: {}'.format(nomevelho))
print('Existe {} mulher(es) com menos de 20 anos.'.format(qtmulher))