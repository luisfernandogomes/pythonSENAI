import random
def par_ou_impar():
    print("bem vindo ao jogo")

    def menu():
        print("bem vindo ao jogo de par ou impar")
        print("="*50)

        print("="*50)
        print("escolha par ou impar e insira um numero de 1 a 5")
    def solicita_nome():
        name = input("insira seu nickname para uma melhor interface")
        return name
    name = solicita_nome()
    pontuacao_user = 0
    pontuacao_cpu = 0
    menu = menu()

    while True:
        try:
            def escolha_do_usuario():
                while True:
                    try:
                        usuario_escolha = int(input("\nvocê deseja ser par ou ímpar?\n[1] ímpar\n[2] par"))
                        return usuario_escolha
                    except ValueError:
                        print("tente novamente com os valores indicados. [1] ou [2]")
            usuario_escolha = escolha_do_usuario()
            numero_aleatorio = random.randint(1,5)


            if usuario_escolha == 1:
                print(f"ok, {name} selecionou ímpar")
                def recebe_numero_usuario():
                    while True:
                        try:
                            numero_usuario = int(input("insira um numero de 1 a 5"))
                            if numero_usuario in range(1,5):
                                return numero_usuario
                            else:
                                print("tente novamente com os valores indicados")
                        except ValueError:
                            print("tente novamente com os valores indicados. ex: 1 , 2, 3, 4, 5")
                numero_usuario = recebe_numero_usuario()
                total = numero_usuario + numero_aleatorio
                print(f"CPU: {numero_aleatorio} + user: {numero_usuario} = {total}")
                if total % 2 == 0:
                    print("ponto para cpu")
                    pontuacao_cpu += 1
                else:
                    print(f"ponto para {name}")
                    pontuacao_user += 1
            elif usuario_escolha == 2:
                print(f"ok, {name} é par")
                numero_usuario
                total = numero_usuario + numero_aleatorio
                print(f"CPU: {numero_aleatorio} + user: {numero_usuario} = {total}")
                if total % 2 == 0:
                    print(f"ponto para {name}")
                    pontuacao_user += 1
                else:
                    print(f"ponto para cpu")
                    pontuacao_cpu += 1


            while True:

                try:
                    jogar_novamente = int(input("deseja jogar novamente?\n[0] sair\n[1] jogar novamente\n"))
                    if jogar_novamente == 0:
                        break
                    elif jogar_novamente ==1:
                        break
                    else:
                        print("valor incorreto, tente novamente")
                except ValueError:
                    print("tente novamente, um valor válido")

            if jogar_novamente == 0:
                print(f"pontuação\nCPU: {pontuacao_cpu}\n{name}: {pontuacao_user}")
                if pontuacao_cpu > pontuacao_user:
                    print("poxa, não foi dessa vez, infelismente eu ganhei de você")
                    print(f"{name} obrigado por jogar\nencerrando o programa...")
                    break
                elif pontuacao_cpu < pontuacao_user:
                    print(f"parabens {name} você foi o vencedor")
                    print(f"{name} obrigado por jogar\nencerrando o programa...")
                    break
                else:
                    print("parabens! parece que estamos no mesmo nível 😊😊")
                    break
        except ValueError:
            print("valor incorreto, por favor insira um valor valido")