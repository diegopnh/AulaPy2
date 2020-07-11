valores = list()
pergunta = "S"

while pergunta == "S":
    adicao = int(input("Digite um valor: ")) 
    if adicao in valores:
        print('Esse número já existe na lista! Inclua outro valor.')
    else:
        valores.append(adicao)
        print('Valor incluso com sucesso!')
    pergunta = str(input("Quer continuar? [S/N]: ")).upper()

print(sorted(valores))


