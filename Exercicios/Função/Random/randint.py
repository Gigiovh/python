'''PEDRA PAPEL TESOURA'''
from random import randint

itens = ( 'Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)

print('''Suas opções são:
[0]- Papel
[1] - Pedra
[2] - Tesoura''')
jogador= int(input('Qual a sua jogada ?'))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador ==0:
    if jogador  ==0:
        print('Empate')
    elif jogador ==1:
        print('Jogador perdeu!')
    elif jogador ==2:
        print('Jogador venceu!')
    else:
        print('Jogador inválida')
if computador ==1:
    if jogador  ==1:
        print('Empate')
    elif jogador ==0:
        print('Jogador venceu!')
    elif jogador ==2:
        print('Jogador perdeu!')
    else:
        print('Jogador inválida')
        if computador == 2:
            if jogador == 2:
                print('Empate')
            elif jogador == 0:
                print('Jogador perdeu!')
            elif jogador == 1:
                print('Jogador venceu!')
            else:
                print('Jogador inválida')

