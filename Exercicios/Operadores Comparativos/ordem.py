#Ordem  de 5 números
n1=int(input('Digite um número: '))
n2=int(input('Digite um número : '))
n3=int(input('Digite um número : '))
n4=int(input('Digite um número : '))
n5=int(input('Digite um número : '))
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
   Maior=n1
elif n1<n2 and n2<n3 and n3<n4 and n4<n5:
   Maior=n5
elif n3>n2 and n3>  n1 and n3> n4 and n3 >n5:
   Maior = n3
elif n4 > n2 and n4 > n1 and n3 < n4 and n4 > n5:
   Maior = n4
else:
    Maior = n5

if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        Menor = n1
elif n1 > n2 and n2 > n3 and n3 > n4 and n4 > n5:
        Menor = n5
elif n3 < n2 and n3 < n1 and n3 < n4 and n3 < n5:
        Menor = n3
elif n4 < n2 and n4 < n1 and n3 < n4 and n4 < n5:
        Menor = n4
else:
        Menor = n5
