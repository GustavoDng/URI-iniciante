x = float(input())
x = x + 0.001
print('NOTAS:')

centena = int(x/100)
x = (x-(centena*100))

print('%d nota(s) de R$ 100.00' %centena)

cinquenta = int(x/50)
x = (x-(cinquenta*50))

print('%d nota(s) de R$ 50.00' %cinquenta)

vinte = int(x/20)
x = (x-(vinte*20))

print('%d nota(s) de R$ 20.00' %vinte)

dez = int(x/10)
x= (x-(dez*10))

print('%d nota(s) de R$ 10.00' %dez)

cinco = int(x/5)
x = (x-(cinco*5))

print('%d nota(s) de R$ 5.00' %cinco)

dois = int(x/2)
x = (x-(dois*2))

print('%d nota(s) de R$ 2.00' %dois)

print('MOEDAS:')

um = int(x)
x = (x-um)

print('%d moeda(s) de R$ 1.00' %um)

cinquenta_centavos = int(x/0.5)
x = (x-(cinquenta_centavos*0.5))

print('%d moeda(s) de R$ 0.50' %cinquenta_centavos)

vinte_e_cinco_centavos = int(x/0.25)
x = (x-(vinte_e_cinco_centavos*0.25))

print('%d moeda(s) de R$ 0.25' %vinte_e_cinco_centavos)

dez_centavos = int(x/0.1)
x = (x-(dez_centavos*0.1))

print('%d moeda(s) de R$ 0.10' %dez_centavos)

cinco_centavos = int(x/0.05)
x = (x-(cinco_centavos*0.05))

print('%d moeda(s) de R$ 0.05' %cinco_centavos)

x = int(x/0.01)

print('%d moeda(s) de R$ 0.01' %x)