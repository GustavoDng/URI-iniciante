x = input().split(' ')

x1, x2, x3 = x

x1 = float(x1)
x2 = float(x2)
x3 = float(x3)

lista = [x1,x2,x3]

lista.sort()

if lista[2] < (lista[0]+lista[1]):
    perimetro = x1+x2+x3
    print('Perimetro = %.1f' %perimetro)
else:
    area = ((x1+x2)*x3)/2
    print('Area = %.1f' %area)