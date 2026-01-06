#emprestimo
n1=float(input('Digite o  valor da casa :'))
n2= float(input('Digite em quantos anos você irá pagar a casa:'))
n3= float(input('Digite o valor do seu salário:'))
n=(n3/100)*30
p= n1/n3
if p<= n:
    print('Você pode fazer o empréstimo')
else:

    print('Você não pode fazer o empréstimo')
