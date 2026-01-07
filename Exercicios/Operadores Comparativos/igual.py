#gênero
nm=str(input('Digite o seu nome:'))
sex=str(input('Digite o seu sexo \n sendo ele:m, para masculino e f ou F para feminino  :'))
id=int(input('Digite a sua idade:'))
if sex=='F' and id<25:
    print('Aceita')
elif sex=='f'and id<25:
    print('Aceita')
else:
    print('Não aceita')
