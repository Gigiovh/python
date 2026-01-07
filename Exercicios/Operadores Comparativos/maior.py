#maior que
nas=int(input('Digite o ano de nascimento: '))
anot=int(input('Digite o ano atual: '))
v=anot-nas
if v>0:
    print('A idade da pessoa é: {}'.format(v))
else:
    print('O ano de nascimento não é válido')
