import random
print('=' * 40)
print('este é o jogo de adivinhação')
print('=' * 40)
print("este é um jogo aonde buscamos desafiar o participante")
print('=' * 40)
name = input("insira seu nickname para uma interface mais interativa")

numero_aleatorio = random.randint(1, 100)

print(f"deseja iniciar o jogo? {name} \n[1] sim\n[0] sair")
print("=" * 40)
while True:
    try:
        entrar = int(input("Deseja iniciar o programa? "))
        if entrar in [0, 1]:
            break
        else:
            print("Experimente valores de 0 a 1")
    except ValueError:
        print('Entrada inválida. Por favor, insira 1 ou 0.')
if entrar == 1:
    print("bem vindo ao jogo")
    print('=' * 40)
    print("agora irei lhe dar algumas instruções de como o jogo funciona")
    print(
        "A mecânica do jogo é estruturada da seguinte forma: um número aleatório \né selecionado dentro do intervalo de 0 a 100, e o participante deve empenhar-se \nem deduzir qual é. Para auxiliar nesse processo, serão fornecidas orientações indicativas \nde se o número introduzido pelo participante é superior ou inferior ao número aleatoriamente escolhido. \nEsteja ciente de que tais instruções constituem um elemento crucial para o sucesso na atividade proposta.")
    print("=" * 40)
    print('=' * 40)
    print("iniciando o jogo✨✨✨")
    while entrar == 1:
        while True:
            try:
                numero_do_jogador = int(input("insira um numero de 1 a 100: "))
                if numero_do_jogador > 0 and numero_do_jogador < 101:
                    break

                else:
                    print("Experimente valores de 0 a 100")
            except ValueError:
                print('Entrada inválida. Por favor, insira 1 ou 100.')

        if numero_do_jogador == numero_aleatorio:
            print(f"parabéns você acertou o numero sorteado")

            while True:
                try:
                    entrar = int(input("parabéns você terminou o jogo, deseja jogar novamente? \n[1] sim\n[0] sair"))
                    if entrar == 1:
                        numero_aleatorio = random.randint(0, 100)
                        break
                    elif entrar == 0:
                        break
                    else:
                        print("valor incorreto. tente novamente")
                except ValueError:
                    print("valor incorreto. tente novamente")

        elif numero_do_jogador > numero_aleatorio:
            print("tente novamente, o numero inserido é maior que o numero sorteado")
        elif numero_do_jogador < numero_aleatorio:
            print("tente novamente, o numero inserido é menor que o numero sorteado")

    print(f"obrigado por joga o nosso jogo {name}\nencerrando o programa...")

else:
    print(" encerrando programa")