import datetime

tempo = datetime.datetime.now()
print(tempo)
hora = (tempo.hour)
minuto = (tempo.minute)
segundo = (tempo.second)
print(f"estamos no ano {tempo.year}\nmês {tempo.month}\ndia {tempo.day}\nsão {hora}horas {minuto}minutos {segundo}segundos")

print(tempo.strftime('%A %d %B %Y %I:%M %p'))


hora = (tempo.hour)
minuto = (tempo.minute)
segundo = (tempo.second)
print(hora, minuto, segundo)
if hora in range(0,12):
    print("bom dia")
elif hora in range(12,17):
    print("boa tarde")
elif hora in range(17,23):
    print("boa noite")
