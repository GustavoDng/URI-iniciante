salario = float(input())

if 0 <= salario <= 400:
    novo_salario = salario * 1.15
    reajuste = salario * 0.15
    indice = '15 %'
if 400.01 <= salario <= 800:
    novo_salario = salario * 1.12
    reajuste = salario * 0.12
    indice = '12 %'
if 800.01 <= salario <= 1200:
    novo_salario = salario * 1.10
    reajuste = salario * 0.10
    indice = '10 %'
if 1200.01 <= salario <= 2000:
    novo_salario = salario * 1.07
    reajuste = salario * 0.07
    indice = '7 %'
if salario > 2000:
    novo_salario = salario * 1.04
    reajuste = salario * 0.04
    indice = '4 %'
print('Novo salario: %.2f' %novo_salario)
print('Reajuste ganho: %.2f' %reajuste)
print('Em percentual: %s' %indice)