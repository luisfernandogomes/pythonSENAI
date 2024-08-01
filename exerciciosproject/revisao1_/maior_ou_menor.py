print("maior ou menor")
loop = 1
while loop == 1:
    while True:
        try:
            numero1 = int(input("Digite um numero: "))
            if numero1 <= 0:
                print("Numero invalido")
            else:
                break
        except ValueError:
            print("Numero invalido")
    while True:
        try:
            numero2 = int(input("Digite um numero: "))
            if numero2 <= 0:
                print("Numero invalido")
            else:
                break
        except ValueError:
            print("Numero invalido")
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