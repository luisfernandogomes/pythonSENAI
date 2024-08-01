from datetime import datetime


def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


def exibir_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    print("a sua idade é", idade, "anos")


def solicita_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Qual a sua data de nascimento"))
            if ano_nascimento > datetime.now().year:
                print("digite um ano valido")
            else:
                return ano_nascimento
        except ValueError:
            print("insira um valor valido")


#exibir_idade(1997)

ano_nascimento = solicita_ano_nascimento()

exibir_idade(ano_nascimento=ano_nascimento)