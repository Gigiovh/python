#produto
n1=float(input('Digite o valor do produto:'))
if n1<20:
    L=(n1/100)*45
else:
    L=(n1/100)*30


print('O valor do produto com a venda será de:{}'.format(n1+L))
