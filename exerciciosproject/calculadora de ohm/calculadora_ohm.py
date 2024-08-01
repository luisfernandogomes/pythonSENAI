from utils import *
def calculadora_de_ohm():
    print("bem vindo a calculadora de ohm")

    def menu():
        print("Bem vindo ao menu da calculadora de ohm\n[1] Resistência Elétrica \n[2] Tensão Elétrica \n[3] Corrente Elétrica \n[4] Resistência do Resistor\n[0] Sair")

    def recebe_corrente_final():
        while True:
            try:
                corrente_final = float(input("Digite o valor do corrente: "))
                if corrente_final > 0:
                    return corrente_final
                else:
                    print("insira um valor positivo")
            except ValueError:
                print("insira valores validos")
    # solicita ao usuario o valor da resistencia
    def recebe_resistencia():
        while True:
            try:
                resistencia = float(input("insira o valor da resistencia"))
                if resistencia > 0:
                    return resistencia

            except ValueError:
                print("tente novamnete entre os valores indicados")

    # solicita ao usuario o valor da tensão
    def recebe_tensao():
        while True:
            try:
                tensao = float(input("insira o valor da tensao"))
                if tensao > 0:
                    return tensao

            except ValueError:
                print("tente novamnete com valores númericos")

    # solicita ao usuario o valor da corrente
    def recebe_corrente():
        while True:
            try:
                corrente = float(input("insira o valor da corrente"))
                if corrente > 0:
                    return corrente

            except ValueError:
                print("tente novamente com valores númericos")

    # necessarios para descobrir o resistor necessario
    def tensao_do_dispositivo_final():
        while True:
            try:
                tensao_do_dispositivo = float(input("insira o valor da tensao do dispositivo"))
                if tensao_do_dispositivo > 0:
                    return tensao_do_dispositivo

            except ValueError:
                print("insira o valor da tensao do dispositivo em valores númericos")
    def recebe_resistencia_da_fonte():
        while True:
            try:
                resistencia_do_dispositivo_final = float(input("insira o valor da resistencia da fonte"))
                if resistencia_do_dispositivo_final > 0:
                    return resistencia_do_dispositivo_final

            except ValueError:
                print("tente novamente com valores númericos")

    # tensão = resistencia * corrente
    # corrente = tensão / resistencia
    # resistencia = tensão dividida pela corrente
    # para descobrir o resistor é necessario fazer a seguinte conta: tensaofonte / tensaofinal depois o resultado dividido pela corrente final

    # exibi o mennu e pergunta qual operação deseja realizar
    def qual_operação_descobrir():
        while True:
            try:
                menu()
                operacao = float(input("insira qual opção você deseja"))
                if operacao >= 0 and operacao <= 4:
                    return operacao
            except ValueError:
                print("tente com valores númericos, ex: 2")


    def calcula_resistencia_a_partir_da_tensao_e_corrente(tensao, corrente):
        resistencia = tensao / corrente
        return resistencia

    def calcula_tensao_a_partir_da_resistencia_e_corrente(resistencia, corrente):
        tensao = resistencia / corrente
        return tensao

    def calcula_corrente_a_partir_da_tensao_e_resistencia(resistencia, tensao):
        corrente = tensao / resistencia
        return corrente

    def descobrir_valor_d_resistor_apartir_da_tensao_fonte_etensao_final_e_corrente_final(tensao_da_fonte, tensao_do_dispositivo_final,corrente_da_resistencia):
        resistor = (tensao_da_fonte / tensao_do_dispositivo_final) * corrente_da_resistencia
        return resistor
    operacao = qual_operação_descobrir()
    if operacao == 1:
        tensao = recebe_tensao()
        corrente = recebe_corrente()
        print(calcula_tensao_a_partir_da_resistencia_e_corrente(tensao, corrente))
    elif operacao == 2:
        resistencia = recebe_resistencia()
        corrente = recebe_corrente()
        print(calcula_tensao_a_partir_da_resistencia_e_corrente(resistencia, corrente))
    elif operacao == 3:
        tensao = recebe_tensao()
        corrente = recebe_corrente()
        print(calcula_corrente_a_partir_da_tensao_e_resistencia(tensao, corrente))
    elif operacao == 4:
        resistencia_fonte = recebe_resistencia_da_fonte()
        tensao = recebe_tensao()
        corrente = recebe_corrente_final()
        print(descobrir_valor_d_resistor_apartir_da_tensao_fonte_etensao_final_e_corrente_final(resistencia_fonte, tensao, corrente))