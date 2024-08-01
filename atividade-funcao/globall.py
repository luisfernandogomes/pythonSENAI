from datetime import date
import datetime
import random
horas = datetime.datetime.now().hour

def solicita_nome():
        while True:
            try:
                name = input('insira seu nome para uma interface mais interativa')
                if name.isalpha():
                    return name
                else:
                    print("insira seu nome sem números, ex: Luis")
            except ValueError:
                print("insira seu nome sem letras, ex: Luis")
name = solicita_nome()
def bom_dia(name):

    def bom_dia(name):
        print(f"Bom dia {name}")

    def boa_tarde(name):
        print(f"Boa tarde {name}")

    def boa_noite(name):
        print(f"Boa noite {name}")

    def boa_madrugada(name):
        print(f"Boa madrugada {name}")

    if 0 <= horas <= 5:
        boa_madrugada(name)
    elif 6 <= horas <= 12:
        bom_dia(name)
    elif 12 <= horas <= 18:
        boa_tarde(name)
    elif 18 <= horas <= 24:
        boa_noite(name)
def verificador_de_notas(name):
    while True:
        print("Verificador de nota")

        def recebe_nota1():
            while True:
                try:
                    nota1 = float(input("Digite a primeira nota: "))
                    if 0 <= nota1 <= 10:
                        return nota1
                    else:
                        print("Insira uma nota válida entre 0 e 10")
                except ValueError:
                    print("Insira um valor válido entre 0 e 10")
        nota1 = recebe_nota1()
        def recebe_nota2():
            while True:
                try:
                    nota2 = float(input("Digite a segunda nota: "))
                    if 0 <= nota2 <= 10:
                        return nota2
                    else:
                        print("Insira uma nota válida entre 0 e 10")
                except ValueError:
                    print("Insira um valor válido entre 0 e 10")
        nota2 = recebe_nota2()
        soma = nota1 + nota2
        media = soma / 2

        if media >= 7:
            print(f"{name} você foi Aprovado")
        else:
            print(f"{name} você foi Reprovado")

        while True:
            try:
                loop = int(input("Quer continuar? \n1 [sim]\n0 [sair]\n "))
                if loop == 1 or loop == 0:
                    break
                else:
                    print("Insira 1 para verificar outro número ou 0 para sair")
            except ValueError:
                print("Insira um valor válido (1 para verificar outro número ou 0 para sair)")

        if loop == 0:
            break
def dias_da_semana(name):
    def menu():
        print("Bem-vindo ao exibidor de dia da semana de acordo com número")
    menu()
    loop = 1

    while loop == 1:
        def selecionar_o_dia():
            while True:
                try:
                    dia = int(input("Insira um número de acordo com o dia da semana entre 1 e 7: "))
                    if dia in range(1, 8):
                        return dia
                    else:
                        print("Insira um número entre 1 e 7")
                except ValueError:
                    print("Insira um valor válido entre 1 e 7")
        dia = selecionar_o_dia()
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
                    return loop
                else:
                    print("Insira 1 ou 0")
            except ValueError:
                print("Insira um valor válido: 1 para verificar outro número ou qualquer outro número para sair")
def imposto_de_renda(name):
    loop = 1
    while loop == 1:
        print("Bem-vindo ao calculador de Imposto de Renda")

        def renda_anual():
            while True:
                try:
                    renda_anual = float(input("Por favor, digite o valor de sua renda anual bruta: "))
                    if renda_anual >= 0:
                        return renda_anual
                    else:
                        print("Insira um valor válido para a renda anual (maior ou igual a zero).")
                except ValueError:
                    print("Insira um valor numérico válido para a renda anual.")
        renda_anual = renda_anual()
        # Calcula o imposto devido com base na renda anual e nas faixas de renda
        if renda_anual <= 23820:
            imposto_devido = 0
        elif renda_anual <= 85528:
            imposto_devido = (renda_anual - 23820) * 0.075
        elif renda_anual <= 167990:
            imposto_devido = (renda_anual - 85528) * 0.15 + (85528 - 23820) * 0.075
        elif renda_anual <= 249051:
            imposto_devido = (renda_anual - 167990) * 0.225 + (167990 - 85528) * 0.15 + (85528 - 23820) * 0.075
        else:
            imposto_devido = (renda_anual - 249051) * 0.275 + (249051 - 167990) * 0.225 + (167990 - 85528) * 0.15 + (85528 - 23820) * 0.075

        print(f"O desconto do Imposto de Renda para uma renda anual bruta de R${renda_anual:.2f} é de R${imposto_devido:.2f}.")

        continuar = input("Deseja calcular o Imposto de Renda novamente?\n1 - Repetir\n0 - Sair\n")
        if continuar != '1':
            loop = 0
def maior_de_idade(name):


    print("verificador de idade")
    ano_atual = date.today().year
    loop = 1
    while loop == 1:
        def idade():
            while True:
                try:
                    idade = int(input("Digite seu ano de nascimento: "))
                    if idade > 2019:
                        print("insira uma idade valida, impossivel você ter essa idade")
                    elif idade < 1920:
                        print("impossivel você ter está idade, + que 100 anos🤨")
                    else:
                        return idade
                except ValueError:
                    print("por favor insira um valor valido em número entre 1920 e 2019")
        idade = idade()
        calculo = ano_atual - idade
        if calculo > 18:
            print("você é maior de idade")
        else:
            print("você é de menor de idade")
        while True:
            try:

                loop = int(input("Quer continuar? \n1 [sim]\n0 [sair]\n "))
                if loop == 1:
                    break
                elif loop == 0:
                    break
                else:
                    print("insira 1 ou 0")
            except ValueError:
                print("insira uma valor valido 1 para verificar outro numero\nou qualquer outro número para sair")
def maior_ou_menor(name):
    print("maior ou menor")
    loop = 1
    while loop == 1:
        def numero1():
            while True:
                try:
                    numero1 = int(input("Digite um numero: "))
                    if numero1 <= 0:
                        print("Numero invalido")
                    else:
                        break
                except ValueError:
                    print("Numero invalido")
        numero1 = numero1()
        def numero2():
            while True:
                try:
                    numero2 = int(input("Digite um numero: "))
                    if numero2 <= 0:
                        print("Numero invalido")
                    else:
                        return numero2
                except ValueError:
                    print("Numero invalido")
        numero2 = numero2()
        if numero1 == numero2:
            print(f"{numero1} e {numero2} são iguais ")

        elif numero1 > numero2:
            print(f"{numero1} é maior")
        elif numero2 > numero1:
            print(f"{numero2} é maior")
        while True:
            try:

                loop = int(input("Quer continuar? \n1 [sim]\n0 [sair]\n "))
                if loop == 1:
                    break
                elif loop == 0:
                    break
                else:
                    print("insira 1 ou 0")
            except ValueError:
                print("insira uma valor valido 1 para verificar outro numero\nou qualquer outro número para sair")
def numero_meses(name):
    print("Bem-vindo ao exibidor de mês de acordo com número")
    loop = 1

    while loop == 1:
        while True:
            try:
                dia = int(input("Insira um número de acordo com meses entre 1 e 12: "))
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
def o_maior(name):
    print("Bem-vindo ao verificador de números")
    loop = 1
    while loop == 1:
        while True:
            try:
                n1 = float(input("Digite o primeiro número: "))
                if n1 > 0:
                    break
                else:
                    print("Insira um número positivo")
            except ValueError:
                print("Insira um número válido")
        while True:
            try:
                n2 = float(input("Digite o segundo número: "))
                if n2 > 0:
                    break
                else:
                    print("Insira um número positivo")
            except ValueError:
                print("Insira um número válido")
        while True:
            try:
                n3 = float(input("Digite o terceiro número: "))
                if n3 > 0:
                    break
                else:
                    print("Insira um número positivo")
            except ValueError:
                print("Insira um número válido")

        if n1 == n2 and n1 == n3:
            print(f"{n1}, {n2} e {n3} são iguais")
        elif n1 == n3 and n1 > n2:
            print(f"{n1} e {n3} são iguais e maiores que {n2} (primeiro e terceiro número)")
        elif n1 == n2 and n1 > n3:
            print(f"{n1} e {n2} são iguais e maiores que {n3} (primeiro e segundo número)")
        elif n2 == n3 and n2 > n1:
            print(f"{n2} e {n3} são iguais e maiores que {n1} (segundo e terceiro número)")
        elif n1 >= n2 and n1 >= n3:
            print(f"{n1} é o maior (primeiro número)")
        elif n2 >= n1 and n2 >= n3:
            print(f"{n2} é o maior (segundo número)")
        elif n3 >= n1 and n3 >= n2:
            print(f"{n3} é o maior (terceiro número)")
        else:
            print("Não foi possível determinar o maior número.")

        while True:
            try:
                loop = int(input("Quer continuar?\n1 [sim]\n0 [sair]\n"))
                if loop in (0, 1):
                    break
                else:
                    print("Insira 1 ou 0")
            except ValueError:
                print("Insira um número válido")
def positivo(name):
    print("verificador de numero, este programa visa verificar se um número é positivo ou negativo")
    while True:
        while True:
            try:
                numero = int(input("insira um numero"))
                if numero > 0:
                    break
                elif numero < 0:
                    break
            except ValueError:
                print("insira um valor valido")
        if numero > 0:
            print(f"o {numero} é positivo")
        else:
            print("número é negativo")
        while True:
            try:
                loop = input("Quer continuar? [S/N] ")
                if loop == "N":
                    break
                elif loop == "S":
                    break
                else:
                    print("insira um valor valido")
            except ValueError:
                print("insira um valor valido")
def adivinhação_com_vidas(name):
    import random

    # Define loop como 1 para iniciar o jogo
    loop = 1

    # Enquanto loop for igual a 1, o jogo continua
    while loop == 1:

        # Define ganhou como 0, indicando que o jogador ainda não ganhou
        ganhou = 0

        # Gera um número secreto aleatório entre 1 e 100
        numero_secreto = random.randint(1, 100)

        # Exibe uma mensagem de boas-vindas ao jogador
        print("\nBem vindo ao jogo de adivinha")

        # Loop para obter a dificuldade escolhida pelo jogador
        def escolha():
            while True:
                try:
                    # Solicita ao jogador que escolha uma dificuldade
                    escolha = input("\nQual dificuldade (Difícil, Normal ou Fácil) você deseja seguir? ")
                    if escolha == "Difícil" or escolha == "Dificil" or escolha == "dificil" or escolha == "difícil" or escolha == "Normal" or escolha == "normal" or escolha == "Fácil" or escolha == "Facil" or escolha == "fácil" or escolha == "facil":
                        return escolha
                except ValueError:
                    print("tente novamente com as escolhas indicadas")
        escolha = escolha()
        def vidas(escolha):

            # Verifica a escolha do jogador e define o número de vidas de acordo com a dificuldade
            if escolha == "Difícil" or escolha == "Dificil" or escolha == "dificil" or escolha == "difícil":
                vidas = 5
                return vidas
            elif escolha == "Normal" or escolha == "normal":
                vidas = 10
                return vidas
            elif escolha == "Fácil" or escolha == "Facil" or escolha == "fácil" or escolha == "facil":
                vidas = 15
                return vidas
        vidas = vidas(escolha)
        # Exibe o número de vidas do jogador
        print(f"\nVocê tem {vidas} tentativas.")

        # Loop para o jogo principal
        while vidas != 0:

            # Loop para obter o número solicitado pelo jogador
            def numero_do_jogador():
                while True:
                    try:
                        # Solicita ao jogador que adivinhe um número
                        numero_solicitado = int(input("Ok, agora tente adivinhar um número de 0 a 100: "))

                        # Verifica se o número solicitado está dentro do intervalo válido
                        if numero_solicitado >= 0 and numero_solicitado <= 100:
                            return numero_solicitado
                        else:
                            print("\nescreva corretamente.\n")
                    # Trata erros de valor, como entrada inválida
                    except ValueError:
                        print("\nErro! Tente novamente!")
            numero_solicitado = numero_do_jogador()
            # Verifica se o número solicitado é maior que o número secreto
            if numero_solicitado > numero_secreto:
                print("\nÉ menor que isso.")
                vidas -= 1
                print(f"\nVocê tem {vidas} tentativas.")

            # Verifica se o número solicitado é menor que o número secreto
            elif numero_solicitado < numero_secreto:
                print("\nÉ maior que isso.")
                vidas -= 1
                print(f"\nVocê tem {vidas} tentativas.")

            # Verifica se o número solicitado é igual ao número secreto
            else:
                vidas = 0
                ganhou = 1

        # Verifica se o jogador ganhou
        if ganhou == 1:
            print("\nBoa, você ganhou!")
        else:
            print(f"\nEita, você perdeu!\n o numero era {numero_secreto}")


        # Loop para perguntar ao jogador se deseja jogar novamente
        def loop():
            while True:
                try:
                    # Solicita ao jogador que responda se deseja jogar novamente
                    loop = input("\nDeseja jogar novamente? ")

                    # Verifica a resposta do jogador e define loop de acordo
                    if loop == "Não" or loop == "nao" or loop == "n" or loop == "não" or loop == "Nao":
                        loop = 0
                        return loop
                    elif loop == "Sim" or loop == "sim" or loop == "s":
                        loop = 1
                        return loop
                    else:
                        print("\nescreva corretamente.\n")
                # Trata erros de valor, como entrada inválida
                except ValueError:
                    print("\nErro tente novamente")
        loop = loop()
def calculadora(name):
    def receber_valor_A():
        while True:
            try:
                valor_a = float(input("Digite o primeiro valor: "))
                return valor_a
            except ValueError:
                print("Tente com números. Exemplo: 1")

    def receber_valor_b():
        while True:
            try:
                valor_b = float(input("Digite o segundo valor: "))
                return valor_b
            except ValueError:
                print("Tente com valores numéricos. Exemplo: 1")

    def qual_operacao_realizar():
        while True:
            try:
                qual_operacao = int(input(
                    "Insira \n[1] para somar\n[2] para subtrair\n[3] multiplicação\n[4] divisão\n[5] potenciação: "))
                if 1 <= qual_operacao <= 5:
                    return qual_operacao
                else:
                    print("Tente valores entre 1 e 5.")
            except ValueError:
                print("Tente valores entre 1 e 5. Exemplo: 1")

    def calculadora():
        while True:
            valor_a = receber_valor_A()
            valor_b = receber_valor_b()
            operacao = qual_operacao_realizar()

            if operacao == 1:
                print(f"A soma é: {valor_a + valor_b}")
            elif operacao == 2:
                print(f"A subtração é: {valor_a - valor_b}")
            elif operacao == 3:
                print(f"A multiplicação é: {valor_a * valor_b}")
            elif operacao == 4:
                if valor_b != 0:
                    print(f"A divisão é: {valor_a / valor_b}")
                else:
                    print("Não é possível dividir por zero.")
            elif operacao == 5:
                print(f"A potenciação é: {valor_a ** valor_b}")

            loop = input("Quer continuar? \n[S] continuar\n[qualquer outra tecla] sair ").upper()
            if loop != "S":
                break
def calculadora_de_celsius(name):
    def recebe_celsius():
        while True:
            try:
                celsius = float(input("Insira a temperatura em Celsius: "))
                return celsius
            except ValueError:
                print("Insira a temperatura em números válidos.")

    def transformar_para_oq():
        while True:
            try:
                transforma_em_oq = int(input("Insira \n[1] para transformar em Fahrenheit\n[2] para transformar em Kelvin: "))
                if transforma_em_oq in (1, 2):
                    return transforma_em_oq
                else:
                    print("Tente com valores entre 1 e 2.")
            except ValueError:
                print("Tente com valores entre 1 e 2.")

    def converte_celsius_em_fahrenheit(celsius):
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit

    def converte_celsius_em_kelvin(celsius):
        kelvin = celsius + 273.15
        return kelvin
    loop = "s"
    while loop == "s" or loop == "S" or loop == "sim" or loop == "SIM" or loop == "Sim":
        temp_celsius = recebe_celsius()
        opcao = transformar_para_oq()
        if opcao == 1:
            print(f"{temp_celsius:.2f}°C é igual a {converte_celsius_em_fahrenheit(temp_celsius):.2f}°F")
        elif opcao == 2:
            print(f"{temp_celsius:.2f}°C é igual a {converte_celsius_em_kelvin(temp_celsius):.2f}K")
        while True:
            try:
                loop = input("Quer continuar? [S/N] ").upper()
                if loop == "N" or loop == "n" or loop == "não" or loop == "Não":
                    print("Obrigado por usar o programa!")
                    break
                elif loop == "S":
                    break
                else:
                    print("tente novamente com as opções indicadas")
            except ValueError:
                print("tente com as opções indicadas")
def calculadora_de_imc(name):
    def recebe_peso():
        while True:
            try:
                peso = float(input("insira o seu peso: "))
                if peso > 0:
                    return peso
            except ValueError:
                print("Por favor, insira um valor inteiro")
    def classificação(imc):
        if imc < 18.5:
            msg = "Abaixo do peso"
        elif imc < 25:
            msg = "Peso ideal"
        elif imc < 30:
            msg = "Sobrepeso"
        elif imc < 34:
            msg = "Obesidade primeiro grau"
        elif imc < 40:
            msg = "Obesidade segundo grau"
        else:
            msg = "Obesidade terceiro grau"
        return msg
    def recebe_altura():
        while True:
            try:
                altura = float(input("insira o seu altura em metros: "))
                if altura > 1 and altura < 2.5:
                    return altura
                else:
                    print("Por favor, insira como no exemplo: 1.5")
            except ValueError:
                print("Por favor, insira em metros, insira como no exemplo: 1.8")
    def calculo(peso,altura):
        imc = peso / (altura * altura)
        return imc
    imc = calculo(recebe_peso(),recebe_altura())

    print(imc)
    print(classificação(imc))
def triangulo(name):
    def recebe_valor_a():
        while True:
            try:
                valor_a = float(input('Digite primeiro valor: '))
                if valor_a < 0:
                    print("Insira valores acima de 0")
                else:
                    return valor_a
            except ValueError:
                print("Tente novamente com números. Exemplo: 2")


    def recebe_valor_b():
        while True:
            try:
                valor_b = float(input('Digite segundo valor: '))
                if valor_b < 0:
                    print("Insira valores acima de 0")
                else:
                    return valor_b
            except ValueError:
                print("Tente novamente com números. Exemplo: 2")


    def recebe_valor_c():
        while True:
            try:
                valor_c = float(input('Digite terceiro valor: '))
                if valor_c < 0:
                    print("Insira valores acima de 0")
                else:
                    return valor_c
            except ValueError:
                print("Tente novamente com números. Exemplo: 2")


    valor_a = recebe_valor_a()
    valor_b = recebe_valor_b()
    valor_c = recebe_valor_c()

    x = valor_a
    y = valor_b
    z = valor_c

    if x == y == z:
        print("Triângulo equilátero")
    elif x == y or y == z or z == x:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
def par_ou_impar(name):
    print("bem vindo ao jogo")

    def menu():
        print("bem vindo ao jogo de par ou impar")
        print("=" * 50)

        print("=" * 50)
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
            numero_aleatorio = random.randint(1, 5)

            if usuario_escolha == 1:
                print(f"ok, {name} selecionou ímpar")

                def recebe_numero_usuario():
                    while True:
                        try:
                            numero_usuario = int(input("insira um numero de 1 a 5"))
                            if numero_usuario in range(1, 5):
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
                    elif jogar_novamente == 1:
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

def calculadora_de_ohm():
    print("bem vindo a calculadora de ohm")

    def menu():
        print(
            "Bem vindo ao menu da calculadora de ohm\n[1] Resistência Elétrica \n[2] Tensão Elétrica \n[3] Corrente Elétrica \n[4] Resistência do Resistor\n[0] Sair")

    def recebe_corrente_final():
        while True:
            try:
                corrente_final = float(input("Digite o valor do corrente: "))
                if corrente_final > 0:
                    return corrente_final
                else:
                    print("insira um valor positivo")
            except ValueError:
                print("insira valores validos")

    # solicita ao usuario o valor da resistencia
    def recebe_resistencia():
        while True:
            try:
                resistencia = float(input("insira o valor da resistencia"))
                if resistencia > 0:
                    return resistencia

            except ValueError:
                print("tente novamnete entre os valores indicados")

    # solicita ao usuario o valor da tensão
    def recebe_tensao():
        while True:
            try:
                tensao = float(input("insira o valor da tensao"))
                if tensao > 0:
                    return tensao

            except ValueError:
                print("tente novamnete com valores númericos")

    # solicita ao usuario o valor da corrente
    def recebe_corrente():
        while True:
            try:
                corrente = float(input("insira o valor da corrente"))
                if corrente > 0:
                    return corrente

            except ValueError:
                print("tente novamente com valores númericos")

    # necessarios para descobrir o resistor necessario
    def tensao_do_dispositivo_final():
        while True:
            try:
                tensao_do_dispositivo = float(input("insira o valor da tensao do dispositivo"))
                if tensao_do_dispositivo > 0:
                    return tensao_do_dispositivo

            except ValueError:
                print("insira o valor da tensao do dispositivo em valores númericos")

    def recebe_resistencia_da_fonte():
        while True:
            try:
                resistencia_do_dispositivo_final = float(input("insira o valor da resistencia da fonte"))
                if resistencia_do_dispositivo_final > 0:
                    return resistencia_do_dispositivo_final

            except ValueError:
                print("tente novamente com valores númericos")

    # tensão = resistencia * corrente
    # corrente = tensão / resistencia
    # resistencia = tensão dividida pela corrente
    # para descobrir o resistor é necessario fazer a seguinte conta: tensaofonte / tensaofinal depois o resultado dividido pela corrente final

    # exibi o mennu e pergunta qual operação deseja realizar
    def qual_operação_descobrir():
        while True:
            try:
                menu()
                operacao = float(input("insira qual opção você deseja"))
                if operacao >= 0 and operacao <= 4:
                    return operacao
            except ValueError:
                print("tente com valores númericos, ex: 2")

    def calcula_resistencia_a_partir_da_tensao_e_corrente(tensao, corrente):
        resistencia = tensao / corrente
        return resistencia

    def calcula_tensao_a_partir_da_resistencia_e_corrente(resistencia, corrente):
        tensao = resistencia / corrente
        return tensao

    def calcula_corrente_a_partir_da_tensao_e_resistencia(resistencia, tensao):
        corrente = tensao / resistencia
        return corrente

    def descobrir_valor_d_resistor_apartir_da_tensao_fonte_etensao_final_e_corrente_final(tensao_da_fonte,
                                                                                          tensao_do_dispositivo_final,
                                                                                          corrente_da_resistencia):
        resistor = (tensao_da_fonte / tensao_do_dispositivo_final) * corrente_da_resistencia
        return resistor

    operacao = qual_operação_descobrir()
    if operacao == 1:
        tensao = recebe_tensao()
        corrente = recebe_corrente()
        print(calcula_tensao_a_partir_da_resistencia_e_corrente(tensao, corrente))
    elif operacao == 2:
        resistencia = recebe_resistencia()
        corrente = recebe_corrente()
        print(calcula_tensao_a_partir_da_resistencia_e_corrente(resistencia, corrente))
    elif operacao == 3:
        tensao = recebe_tensao()
        corrente = recebe_corrente()
        print(calcula_corrente_a_partir_da_tensao_e_resistencia(tensao, corrente))
    elif operacao == 4:
        resistencia_fonte = recebe_resistencia_da_fonte()
        tensao = recebe_tensao()
        corrente = recebe_corrente_final()
        print(descobrir_valor_d_resistor_apartir_da_tensao_fonte_etensao_final_e_corrente_final(resistencia_fonte, tensao,corrente))
loop = 1
while loop == 1:
    while True:
        try:
            def menu():
                print('-'*40)
                print("bem vindo a central de atividades já realizadas com python")
                print('-'*40)
                print("\n[0] sair\n[1] verificador de nota\n[2] dias da semana\n[3] imposto de renda\n[4] maior de idade\n[5] maior ou menor\n[6] meses\n[7] o maior\n[8] positivo ou negativo\n[9] adivinhação com vidas\n[10] bom dia\n[11] calculadora\n[12] calculadora_de_celsius\n[13] calculadora_de_imc\n[14] triangulo\n[15] calculadora de ohm\n[16] par ou impar")
                print('-'*40)
            name
            menu = menu()
            escolha = int(input("escolha qual opção deseja"))
            if escolha == 1:
                verificador_de_notas()
            elif escolha == 2:
                dias_da_semana()
            elif escolha == 3:
                imposto_de_renda()
            elif escolha == 4:
                maior_de_idade()
            elif escolha == 5:
                maior_ou_menor()
            elif escolha == 6:
                numero_meses()
            elif escolha == 7:
                o_maior()
            elif escolha == 8:
                positivo()
            elif escolha == 9:
                adivinhação_com_vidas()
            elif escolha == 10:
                bom_dia()
            elif escolha == 11:
                calculadora()
            elif escolha == 12:
                calculadora_de_celsius()
            elif escolha == 13:
                calculadora_de_imc()
            elif escolha == 14:
                triangulo()
            elif escolha == 15:
                calculadora_de_ohm()

            elif escolha == 0:
                break

            else:
                print("insira apenas os valores indicados no menu")
        except ValueError:
            print("escolha invalida")
    while True:
        try:
            loop = int(input("tem certeza que não quer continuar?\n[1] sim\n[0] sair\n"))
            if loop in (0, 1):
                break
            else:
                print("Insira 1 ou 0")
        except ValueError:
            print("Insira um número válido")