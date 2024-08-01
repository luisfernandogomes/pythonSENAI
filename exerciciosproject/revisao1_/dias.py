print("Bem-vindo ao exibidor de dia da semana de acordo com número")
loop = 1

while loop == 1:
    while True:
        try:
            dia = int(input("Insira um número de acordo com o dia da semana entre 1 e 7: "))
            if dia in range(1, 8):
                break
            else:
                print("Insira um número entre 1 e 7")
        except ValueError:
            print("Insira um valor válido entre 1 e 7")

    if dia == 1:
        print("Hoje é segunda-feira")
    elif dia == 2:
        print("Hoje é terça-feira")
    elif dia == 3:
        print("Hoje é quarta-feira")
    elif dia == 4:
        print("Hoje é quinta-feira")
    elif dia == 5:
        print("Hoje é sexta-feira")
    elif dia == 6:
        print("Hoje é sábado")
    elif dia == 7:
        print("Hoje é domingo")
    else:
        print("Número inválido. Digite um número entre 1 e 7.")

    while True:
        try:
            loop = int(input("Quer continuar?\n1 [sim]\n0 [sair]\n"))
            if loop in (0, 1):
                break
            else:
                print("Insira 1 ou 0")
        except ValueError:
            print("Insira um valor válido: 1 para verificar outro número ou qualquer outro número para sair")
