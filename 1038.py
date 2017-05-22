pedido = input().split(' ')

item, quantidade = pedido

item = int(item)
quantidade = int(quantidade)

if item == 1:
    item = 4.00
elif item == 2:
    item = 4.50
elif item == 3:
    item = 5.00
elif item == 4:
    item = 2
elif item == 5:
    item = 1.50


conta = item*quantidade
print('Total: R$ %.2f' %conta)