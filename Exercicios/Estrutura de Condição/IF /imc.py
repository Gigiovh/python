#peso
n1=float(input('Digite a quanto você tem de altura:'))
n2=float(input('Digite o seu peso:'))
imc= n2 / (n1 ** 2)
if imc <18.5:
    print('Você está abaixo do peso')
elif imc>18.5 and imc <25:
    print('Você está no peso ideal')
elif imc> 25 and imc <30:
    print('Você está com Sobrepeso')
elif imc>30 and imc <40:
    print('Você está obeso')
else:

    print('Você está com obesidade mórbita')
