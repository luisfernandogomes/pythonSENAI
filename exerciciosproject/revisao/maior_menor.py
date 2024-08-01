while True:
    try:
        number1 = int("insira um número")
        if number1 > 1:
            break
        else:
            print("insira um número inteiro positivo")
    except ValueError:
        print("insira um valor valido")
    try:
        number2 = int("insira um número")
        if number2 > 1:
            break
        else:
            print("insira um valor inteiro positivo")
    except ValueError:
        print("insira um valor valido")
    if number1 == number2:
        print("os número são iguais")
        break
    elif number1 > number2:
        print("numero 1 é maior que numero 2")
        break
    else:
        print("número 2 é maior que numero 1")
        break
    break