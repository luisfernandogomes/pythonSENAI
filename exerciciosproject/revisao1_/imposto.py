loop = 1
while loop == 1:
    print("Bem-vindo ao calculador de Imposto de Renda")

    while True:
        try:
            renda_anual = float(input("Por favor, digite o valor de sua renda anual bruta: "))
            if renda_anual >= 0:
                break
            else:
                print("Insira um valor válido para a renda anual (maior ou igual a zero).")
        except ValueError:
            print("Insira um valor numérico válido para a renda anual.")

    # Calcula o imposto devido com base na renda anual e nas faixas de renda
    if renda_anual <= 23820:
        imposto_devido = 0
    elif renda_anual <= 85528:
        imposto_devido = (renda_anual - 23820) * 0.075
    elif renda_anual <= 167990:
        imposto_devido = (renda_anual - 85528) * 0.15 + (85528 - 23820) * 0.075
    elif renda_anual <= 249051:
        imposto_devido = (renda_anual - 167990) * 0.225 + (167990 - 85528) * 0.15 + (85528 - 23820) * 0.075
    else:
        imposto_devido = (renda_anual - 249051) * 0.275 + (249051 - 167990) * 0.225 + (167990 - 85528) * 0.15 + (85528 - 23820) * 0.075

    print(f"O desconto do Imposto de Renda para uma renda anual bruta de R${renda_anual:.2f} é de R${imposto_devido:.2f}.")

    continuar = input("Deseja calcular o Imposto de Renda novamente?\n1 - Repetir\n0 - Sair\n")
    if continuar != '1':
        loop = 0