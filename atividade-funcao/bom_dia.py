import datetime
# Madrugada - 0h às 5h - Boa madruga
# Manhã - 5h às 12h - Bom dia
# Tarde - 12h às 19h - Boa tarde
# Noite - 19h às 24h - Boa noite
def bom_dia():
    def recebe_name():
        while True:
            try:
                name = input('Qual o seu nome? ')
                if name.isalpha():
                    return name
                else:
                    print("Insira o nome corretamente, sem números.")
            except ValueError:
                print("Insira seu nome sem números, ex: Luis")
    name = recebe_name()
    horas = datetime.datetime.now().hour
    if 0 <= horas <= 5:
        print(f"Boa madrugada, {name}!")
    elif 6 <= horas <= 12:
        print(f"Bom dia, {name}!")
    elif 12 <= horas <= 18:
        print(f"Boa tarde, {name}!")
    else:
        print(f"Boa noite, {name}!")
bom_dia()