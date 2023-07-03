#Média dos valores digitados
s = 0
for c in range (0,4):
    n = int(input(' Digite a nota da prova:'))
    s+= n
print('A média dos valores é {}'.format(s/4))