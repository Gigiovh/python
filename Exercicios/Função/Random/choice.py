from random import choice

cor1=str(input(' Digite um nome: '))
cor2=str(input(' Digite um nome: '))
cor3=str(input(' Digite um nome: '))

cores=[cor1,cor2,cor3]

escolha= choice(cores)
print(' A pessoa escolhida foi:{} '.format(escolha))
