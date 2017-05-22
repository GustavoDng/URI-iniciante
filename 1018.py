x = int(input())
print('%d' %x)
if x >= 100:
    centena = x/100,
    x = (x % 100)
    print('%d nota(s) de R$ 100,00' %centena)
else:
    print('0 nota(s) de R$ 100,00')
if x >= 50:
    cinquenta = x/50,
    x = (x % 50)
    print('%d nota(s) de R$ 50,00' %cinquenta)
else:
    print('0 nota(s) de R$ 50,00')
if x >= 20:
    vinte = x/20,
    x = (x % 20)
    print('%d nota(s) de R$ 20,00' %vinte)
else:
    print('0 nota(s) de R$ 20,00')
if x >= 10:
    dez = x/10,
    x = (x % 10)
    print('%d nota(s) de R$ 10,00' %dez)
else:
    print('0 nota(s) de R$ 10,00')
if x >= 5:
    cinco = x/5,
    x = (x % 5)
    print('%d nota(s) de R$ 5,00' %cinco)
else:
    print('0 nota(s) de R$ 5,00')
if x >= 2:
    dois = x/2,
    x = (x % 2)
    print('%d nota(s) de R$ 2,00' %dois)
else:
    print('0 nota(s) de R$ 2,00')
if x < 2:
    print('%d nota(s) de R$ 1,00' %x)
else:
    print('0 nota(s) de R$ 1,00')