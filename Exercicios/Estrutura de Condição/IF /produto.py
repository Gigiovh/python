# valor do produto
n1=float(input('Digite o valor do produto:'))
n2=float(input("Digite a forma de pagamento:Se for cheque ,tecle 1 \n Se for a vista e em dinheiro, tecle 2 \n Se for no cartão, á vista , tecle 3 \n Se for no cartão, parcelado em 2 vezes, tecle 4, e se for parcelado em 3 ou mais vezes, tecle 5\n:"))
d= (n1/100)*5
j= (n1/100)*20
d1= n1*10
d11=d1+n1
j1=j+n1
dd=d+n1
if n2 == 1 or n2==2:
    print('O valor do produto será de :{}'.format(d11))
elif n2 == 3 :
    print('O valor do produto será de :{}'.format(dd))
elif n2==4:
    print('O valor do produto será de :{}'.format(n1))
else:
    print('O valor do produto será de :{}'.format(j1))
