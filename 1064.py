n = 0
inteiro = 0
soma = 0


while n < 6:
    x = float(input())
    if x > 0:
        inteiro = inteiro + 1
        soma = soma + x
    n = n + 1

media = soma/inteiro

print('%d valores positivos' %inteiro)
print('%.1f' %media)