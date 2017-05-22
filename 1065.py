n = 0
par = 0

while n < 5:
    x = int(input())
    if (x % 2) == 0:
        par = par + 1
    n = n + 1
print('%d valores pares' %par)