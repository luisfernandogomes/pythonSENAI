def calculadora_de_celsius():
    def recebe_celsius():
        while True:
            try:
                celsius = float(input("Insira a temperatura em Celsius: "))
                return celsius
            except ValueError:
                print("Insira a temperatura em números válidos.")

    def transformar_para_oq():
        while True:
            try:
                transforma_em_oq = int(input("Insira \n[1] para transformar em Fahrenheit\n[2] para transformar em Kelvin: "))
                if transforma_em_oq in (1, 2):
                    return transforma_em_oq
                else:
                    print("Tente com valores entre 1 e 2.")
            except ValueError:
                print("Tente com valores entre 1 e 2.")

    def converte_celsius_em_fahrenheit(celsius):
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit

    def converte_celsius_em_kelvin(celsius):
        kelvin = celsius + 273.15
        return kelvin
    loop = "s"
    while loop == "s" or loop == "S" or loop == "sim" or loop == "SIM" or loop == "Sim":
        temp_celsius = recebe_celsius()
        opcao = transformar_para_oq()
        if opcao == 1:
            print(f"{temp_celsius:.2f}°C é igual a {converte_celsius_em_fahrenheit(temp_celsius):.2f}°F")
        elif opcao == 2:
            print(f"{temp_celsius:.2f}°C é igual a {converte_celsius_em_kelvin(temp_celsius):.2f}K")
        while True:
            try:
                loop = input("Quer continuar? [S/N] ").upper()
                if loop == "N" or loop == "n" or loop == "não" or loop == "Não":
                    print("Obrigado por usar o programa!")
                    break
                elif loop == "S":
                    break
                else:
                    print("tente novamente com as opções indicadas")
            except ValueError:
                print("tente com as opções indicadas")
calculadora_de_celsius()