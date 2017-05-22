tempo = int(input())

if tempo >= 3600:
    horas = int(tempo/3600),
    tempo = int(tempo % 3600)
else:
    horas = 0
if tempo >= 60:
    mintuos = int(tempo/60),
    tempo = int(tempo % 60)
else:
    mintuos = 0
if tempo < 60:
    segundos = int(tempo)

print('%d:' %horas + '%d:' %mintuos + '%d' %segundos)