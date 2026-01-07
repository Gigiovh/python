#Ordem crescente de 3 números
n1=float(input('Digite um número: '))
n2=float(input('Digite um número : '))
n3=float(input('Digite um número : '))
if n1>n2 and n1>n3 and n2>n3:
    print('A ordem crescente dos números é  {}, {}, {}'.format(n3,n2,n1))
elif n1<n2 and n1<n3 and n2>n3:
    print('A ordem crescente dos números é  {}, {}, {}'.format(n1,n3, n2))
elif n1 < n2 and n1 < n3 and n2 < n3:
    print('A ordem crescente dos números é  {}, {}, {}'.format(n1, n2, n3))
else:
    print('A ordem crescente dos números é  {}, {},{}'.format(n1, n2,n3))
