idade_dias =  int(input())

if (idade_dias >= 365):
    idade_anos = int((idade_dias/365))
    idade_dias = (idade_dias % 365)
    print('%d ano(s)' %idade_anos)
else:
    print('0 ano(s)')
if (idade_dias >= 30):
    idade_meses = int(idade_dias/30)
    idade_dias = (idade_dias % 30)
    print('%d mes(es)' %idade_meses)
else:
    print('0 mes(es)')
if (idade_dias < 30):
    print('%d dia(s)' %idade_dias)