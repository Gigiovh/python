#shuffle

from random import shuffle

n1=str(input(' Digite o primeiro elemento da lista: '))
n2=str(input(' Digite o segundo elemento da lista: '))
n3=str(input(' Digite o terceiro elemento da lista: '))

lista= [n1,n2,n3]
shuffle(lista)
print('A lista de elementos é: {}'.format(lista))
