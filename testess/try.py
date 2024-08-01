print("verificador de nota")
loop = 1
while loop == 1:

    while True:
        try:
            nota1 = float(input("Digite a primeira nota: "))
            if nota1 >= 0 and nota1 <= 100:
                break

            else:
                print("insira uma nota valida")
        except ValueError:
            print("insira uma valor valido entre 0 a 10")
    while True:
        try:
            nota2 = float(input("Digite a segunda nota: "))
            if nota2 >= 0 and nota2 <= 100:
                break
            else:
                print("insira uma nota valida entre 0 a 10")
        except ValueError:
            print("insira uma valor valido entre 0 a 10")
    soma = nota1 + nota2
    media = soma / 2
    if media >= 7:
        print("Aprovado")
    elif media < 7:
        print("Reprovado")
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
