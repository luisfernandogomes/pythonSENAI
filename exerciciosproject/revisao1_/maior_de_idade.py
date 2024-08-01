from datetime import date

print("verificador de idade")
ano_atual = date.today().year
loop = 1
while loop == 1:
    while True:
        try:
            idade = int(input("Digite seu ano de nascimento: "))
            if idade > 2019:
                print("insira uma idade valida, impossivel você ter essa idade")
            elif idade < 1920:
                print("impossivel você ter está idade, + que 100 anos🤨")
            else:
                break
        except ValueError:
            print("por favor insira um valor valido em número entre 1920 e 2019")
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