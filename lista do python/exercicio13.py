#porcentagem salario
n1=float(input('Digite o valor do seu salário:'))
s=(n1/100)*10
i=(n1/100)*15
s1= n1 + s
i1= n1 + i
if n1> 1250.00:
    print('O valor do salário será de:{}'.format(s1))
else:
    print('O valor do salário será de:{}'.format(i1))

