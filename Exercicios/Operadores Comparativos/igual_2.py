#Ordem  de 3 números
n1=float(input('Digite um número: '))
n2=float(input('Digite um número : '))
n3=float(input('Digite um número : '))
if n1>n2 and n1>n3:
   Maior=n1
elif n1 < n2 and n2> n3:
    Maior = n2
else:
    Maior = n3
if n1<n2 and n1<n3:
   Menor=n1
elif n1 > n2 and n2< n3:
    Menor = n2
else:
    Menor = n3
if Menor==n3 and Maior==n2:
    Intermediário:n1
elif Menor == n2 and Maior == n3:
    Intermediário: n1
elif Menor == n2 and Maior == n1:
    Intermediário: n3
elif Menor == n1 and Maior == n2:
    Intermediário: n3
else:
    Intermediário==n2
