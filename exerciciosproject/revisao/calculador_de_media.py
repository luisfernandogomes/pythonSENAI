while True:
    try:
        nota1 = int(input("insira sua primeira nota: "))
        if nota1 > 1 or nota1 < 10:
            break
        else:
            print("nota invalida")
    except ValueError:
        print("valor invalido, insira sua nota\nexemplo 8")
    while True:
        try:
            nota2 = int(input("insira sua segunda nota: "))
            if nota2 > 1 and nota2 < 10:
                break
            elif nota2 > 10:
                print("insira uma nota válida")
                print("valor invalido, sua nota de 0 a 10")
        except ValueError:
            print("valor invalido, insira sua nota\nexemplo 8")
    soma = nota1 + nota2
    media = soma / 2
    print(f"sua média foi {media}")
    if media >= 7:
        print("parabéns você foi aprovado")
    else:
        print("você foi reprovado")

