import datetime

name_user = ""
loop = 1
while loop == 1:
    while True:
        def saudacao():
            agr = datetime.datetime.now()
            msg = ""

            if (agr.hour < 12):
                msg = "Bom dia"
            elif (agr.hour < 19):
                msg = "Boa tarde"
            else:
                msg = "Boa noite", agr.hour
            return msg


        name_user = str(input("Digite o nome de usuário: "))
        temp = datetime.datetime.now()


        def mes():
            time = datetime.datetime.now()
            mes_write = ""

            if (time.month == 1):
                mes_write = "Janeiro"
            elif (time.month == 2):
                mes_write = "Fevereiro"
            elif (time.month == 3):
                mes_write = 'Março'
            elif (time.month == 4):
                mes_write = 'Abril'
            elif (time.month == 5):
                mes_write = 'Maio'
            elif (time.month == 6):
                mes_write = 'Junho'
            elif (time.month == 7):
                mes_write = 'Julho'
            elif (time.month == 8):
                mes_write = 'Agosto'
            elif (time.month == 9):
                mes_write = 'Septo'
            elif (time.month == 10):
                mes_write = 'Outubro'
            elif (time.month == 11):
                mes_write = 'Novembro'
            else:
                mes_write = 'Dezembro'
            return mes_write


        print(f"{saudacao()} {name_user}, agora são exatamente: {temp.hour}:{temp.minute} do dia {temp.day} do mês : {mes()}")
        break
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