
from time import sleep
n1= int(input('Digite um número ímpar ou par !! '
              '\n que eu mostrarei a contagem de um deles até 100:'))

teste= n1 % 2

#par
if teste==0:
  for c in range (0,101,2):
      print(c)
      sleep(0.5)
#Ímpar
elif teste!=0:
  for c in range (1,101,2):
      print(c)
      sleep(0.5)

