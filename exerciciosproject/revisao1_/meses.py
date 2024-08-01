print("Bem-vindo ao exibidor de dia da semana de acordo com número")
loop = 1

while loop == 1:
    while True:
        try:
            dia = int(input("Insira um número de acordo com o dia da semana entre 1 e 12: "))
            if dia in range(1, 13):
                break
            else:
                print("Insira um número entre 1 e 12")
        except ValueError:
            print("Insira um valor válido entre 1 e 12")

    if dia == 1:
        print("é janeiro")
    elif dia == 2:
        print("é fevereiro")
    elif dia == 3:
        print("é março")
    elif dia == 4:
        print("é abril")
    elif dia == 5:
        print("é maio")
    elif dia == 6:
        print("é junho")
    elif dia == 7:
        print("é julho")
    elif dia == 8:
        print("é agosto")
    elif dia == 9:
        print("é setembro")
    elif dia == 10:
        print("é outubro")
    elif dia == 11:
        print("é novembro")
    elif dia == 12:
        print("é dezembro")
    else:
        print("Número inválido. Digite um número entre 1 e 12.")

    while True:
        try:
            loop = int(input("deseja realizar outra operação?\n1 [sim]\n0 [sair]\n"))
            if loop in (0, 1):
                break
            else:
                print("Insira 1 ou 0")
        except ValueError:
            print("Insira um valor válido: 1 para verificar outro número ou qualquer outro número para sair")