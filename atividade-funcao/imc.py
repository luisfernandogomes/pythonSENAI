def calculadora_de_imc():
    def recebe_peso():
        while True:
            try:
                peso = float(input("insira o seu peso: "))
                if peso > 0:
                    return peso
            except ValueError:
                print("Por favor, insira um valor inteiro")
    def classificação(imc):
        if imc < 18.5:
            msg = "Abaixo do peso"
        elif imc < 25:
            msg = "Peso ideal"
        elif imc < 30:
            msg = "Sobrepeso"
        elif imc < 34:
            msg = "Obesidade primeiro grau"
        elif imc < 40:
            msg = "Obesidade segundo grau"
        else:
            msg = "Obesidade terceiro grau"
        return msg
    def recebe_altura():
        while True:
            try:
                altura = float(input("insira o seu altura em metros: "))
                if altura > 1 and altura < 2.5:
                    return altura
                else:
                    print("Por favor, insira como no exemplo: 1.5")
            except ValueError:
                print("Por favor, insira em metros, insira como no exemplo: 1.8")
    def calculo(peso,altura):
        imc = peso / (altura * altura)
        return imc
    imc = calculo(recebe_peso(),recebe_altura())

    print(imc)
    print(classificação(imc))
calculadora_de_imc()