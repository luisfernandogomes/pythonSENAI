print("verificador de numero, este programa visa verificar se um número é positivo ou negativo")
while True:
    try:
        numero = int(input("insira um numero"))
        if numero > 0:
            break
        elif numero < 0:
            break
    except ValueError:
        print("insira um valor valido")
if numero > 0:
    print(f"o {numero} é positivo")
else:
    print("número é negativo")