x = input().split(' ')

n1, n2 =  x

n1 = int(n1)
n2= int(n2)

if n1%n2 == 0 or n2%n1 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')