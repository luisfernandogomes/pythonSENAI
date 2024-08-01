while True:
    try:
        number = int("insira um número")
        if number < 0:
            break
        else:
            print("insira um numero positivo")
    except ValueError:
        print("insira um valor válido")

