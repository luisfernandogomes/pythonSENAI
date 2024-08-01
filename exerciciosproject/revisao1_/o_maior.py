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
