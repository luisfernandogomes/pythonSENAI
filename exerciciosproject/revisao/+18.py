calculo = 2024
while True:
    try:
        ano = int(input('Digite seu ano de nascimento: '))
        if ano > 2024:
            break
        elif ano < 1923:
            print("inpossivel você ter idade")
            break
    except ValueError:
        print("digite um valor valido")
    idade = calculo - ano
    if idade < 18:
        print("você é de menor de idade")
        break
    elif idade > 18:
        print("você é de maior de idade")
        break