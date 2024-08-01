print("verificador de numero")
name = input("insira seu nome")
print(f"bem vindo ao verificador {name}")
loop = 1
while loop == 1:
    try:
        number = int(input("insira seu número"))
        if number >= 1:
            print("seu número é positivo")
            break
        else:
            print("seu número é negativo")
            break
    except ValueError:
        print("valor invalido, insira um numero positivo\nexemplo 1")
