n = 0
positivo = 0
negativo = 0
impar = 0
par = 0

while n < 5:
    x = int(input())
    if x > 0:
        positivo = positivo + 1
    if x < 0:
        negativo = negativo + 1
    if (x % 2) == 0:
        par = par + 1
    if (x % 2) == 1:
        impar = impar + 1
    n = n + 1
print('%d valor(es) par(es)' %par)
print('%d valor(es) impar(es)' %impar)
print('%d valor(es) positivo(s)' %positivo)
print('%d valor(es) negativo(s)' %negativo)