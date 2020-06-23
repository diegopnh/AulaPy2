print(20*'-','CADASTRO DE PESSOAS \n',20*'-')
age = int(input('Idade: '))
sex = str(input('Sexo: ')).upper()
bigger = men = woman = 0

while True: 
    contn = (str(input('Você quer continuar? [Y/N]: '))).upper()
    if age >= 18:
        bigger += 1
    if sex == "M":
        men += 1
    if sex == "F" and age < 20:
        woman += 1
    if contn == "Y":
        print('\nCADASTRO DE PESSOAS \n')
        age = int(input('Idade: '))
        sex = str(input('Sexo: ')).upper()
    if contn == "F":
        break

print(f'Total de pessoas com mais de 18: {bigger}')
print(f'Ao todo temos {men} homens cadastrados.')
print(f'E temos {woman} mulher(es) com menos de 20 anos.')

