r = 0
pos = 0

while (r != 6):
    x = float(input())
    r = r + 1
    if x > 0:
        pos = pos + 1
print('%d valores positivos' %pos)