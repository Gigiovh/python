#idade
id=int(input('Digite a sua idade:'))
if id<16:
    print('Não eleitor')
elif id>18 and id<65:
    print('Eleitor obrigátorio')
else:
    print('Eleitor facultativo')
