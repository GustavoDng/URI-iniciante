notas = input().split(' ')

n1, n2, n3, n4 = notas

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10
print('Media: %.1f' %media)

if media >=7:
    print('Aluno aprovado.')
elif media <5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')

    exame = float(input())
    print('Nota do exame: %.1f' %exame)

    media_exame = (exame+media)/2

    if media_exame >= 5:
        print('Aluno aprovado.')
        print('Media final: %.1f' %media_exame)
    if media_exame <=4.9:
        print('Aluno reprovado.')
        print('Media final: %.1f' %media_exame)