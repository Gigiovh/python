#Sálario
s=float(input('Digite o valor do seu salário atual:'))
if s<600 or s==600:
    print('Você está isento do desconto ')
elif s>600 and s<1201:
    D=(s/100)*20
elif s < 1200 and s < 2001:
    D = (s / 100) * 25
else:
    D = (s / 100) * 30
    print('O desconto do salário será de:{}\n O salário total será de:{}'.format(D,s-D))
