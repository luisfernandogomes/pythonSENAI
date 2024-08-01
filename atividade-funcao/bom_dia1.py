import datetime
horas = datetime.datetime.now().hour
def bom_dia():
    def solicita_nome():
        while True:
            try:
                name = input('Qual o seu nome? ')
                if name.isalpha():
                    return name
                else:
                    print("insira seu nome sem números, ex: Luis")
            except ValueError:
                print("insira seu nome sem letras, ex: Luis")

    def bom_dia(name):
        print(f"Bom dia {name}")
    def boa_tarde(name):
        print(f"Boa tarde {name}")
    def boa_noite(name):
        print(f"Boa noite {name}")
    def boa_madrugada(name):
        print(f"Boa madrugada {name}")

    if 0 <= horas <= 5:
        boa_madrugada(solicita_nome())
    elif 6 <= horas <= 12:
            bom_dia(solicita_nome())
    elif 12 <= horas <= 18:
        boa_tarde(solicita_nome())
    elif 18 <= horas <= 24:
        boa_noite(solicita_nome())