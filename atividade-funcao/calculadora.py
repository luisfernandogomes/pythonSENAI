def calculadora():
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
                qual_operacao = int(input("Insira \n[1] para somar\n[2] para subtrair\n[3] multiplicação\n[4] divisão\n[5] potenciação: "))
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

calculadora()