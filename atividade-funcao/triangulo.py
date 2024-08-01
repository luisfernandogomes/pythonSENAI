def triangulo():
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
triangulo()