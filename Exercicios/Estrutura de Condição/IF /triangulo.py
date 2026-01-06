#triangulo
l1=float(input(' medida do triângulo:'))
l2=float(input('Digite a  medida do triângulo:'))
l3=float(input('Digite a  medida do triângulo:'))
if l1==l2 and l1==l3:
  print('O triângulo é equilátero')
elif l1 == l2  and l1 != l3 or l3 == l2 and l3!= l1 or  l1==l3 and l1 != l2:
  print('O triângulo é isosceles')
else:
  print('O triângulo é escaleno')
