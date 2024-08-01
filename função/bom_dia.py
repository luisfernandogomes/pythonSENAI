from datetime import datetime
agora = datetime.now()
print("mensagem automatica")
def solicite_nome():
    while True:
        try:
            name = input("Informe o nome: ")
            if name.isnumeric():
                print("digite apenas letras")
            else:
                return name
        except ValueError:
            print("insira um valor valido")
def hora():
    if agora.hour >= 0 and agora.hour <= 12:
        return print("bom dia")
    elif agora.hour >= 12 and agora.hour <= 18:
        return print("boa tarde")
    else:
        return print("boa noite")



print(solicite_nome()), (hora())