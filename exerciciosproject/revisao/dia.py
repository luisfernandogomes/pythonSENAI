print("insira um número")
while True:
    try:
        number = int(input("insira"))
        if number > 0 and number <= 7:
            print("")
            break
        else:
            print("tente novamente com valore de 1 a 7")
    except ValueError:
        print("tente novamente")


if number == 1:
    print("hoje é segunda")
if number == 2:
    print("hoje é terça")
if number == 3:
    print("hoje é quarta")
if number == 4:
    print("hoje é quinta")
if number == 5:
    print("hoje é sexta")
if number == 6:
    print("hoje é sabado")
if number == 7:
    print("hoje é domingo")