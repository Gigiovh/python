#nadador
n1=int(input('Digite a idade do nadador:'))
if n1 <=9:
    print('Ele é um nadador mirim')
elif n1>9 and n1<14:
    print('Ele é um nadador infantil')
elif n1 >14 and n1<19:
    print('Ele é um nadador junior')
elif n1>19 and n1<25:
    print('Ele é um nadador sênior')
else :

    print('Ele é um nadador master')
