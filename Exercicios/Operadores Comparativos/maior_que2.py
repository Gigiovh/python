#Qual é o maior dos 3?
n1=float(input('Digite um número: '))
n2=float(input('Digite um número : '))
n3=float(input('Digite um número : '))
if n1>n2 and n1>n3:
    print('O número {} é o maior '.format(n1))
elif n1 < n2 and n2 < n3:
    print('O número {} é o maior '.format(n3))
elif n1 < n2 and n2 > n3:
    print('O número {} é o maior '.format(n2))
else:
    print('Os números são iguais')
