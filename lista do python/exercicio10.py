#velocidade
v=float(input('Digite a velocidade do automovél, em Km/h:'))
if v > 80:
  vm = (v - 80) *7
  print('O valor da sua multa será de :{}'.format(vm))
else:
  print('Você não foi multado')