hora = input().split(' ')

h1, h2 = hora

h1 = int(h1)
h2 = int(h2)

if h1 < h2:
    r = h2 - h1
    print('O JOGO DUROU %d HORA(S)' %r)
elif h2 < h1:
    r = (24 - h1) + h2
    print('O JOGO DUROU %d HORA(S)' %r)
else:
    print('O JOGO DUROU 24 HORA(S)')