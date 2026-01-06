#viagem
n1=float(input('Digite a distância de sua viagem wm km:'))
p1=0.50
l1=0.45
p= n1 * p1
l= n1 * l1
if n1<=200:
    print('O valor da passagem será de:{}'.format(p))
else:
    print('O valor da passagem será de :{}'.format(l))
