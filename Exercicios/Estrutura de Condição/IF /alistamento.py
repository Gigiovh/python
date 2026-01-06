#militar
n1=float(input('Digite seu ano de nascimento:'))
n2=float(input('Digite o ano atual:'))
id=n2-n1
al=id-18
if id <18 and id>17:
    print('Você poderá se alistar daqui{} meses'.format(id))
elif id <18 and id < 17:
     print('Você poderá se alistar daqui {} anos'.format(id))
elif id>19 and id <20:
    print('Passou seu prazo de alistamento há {} meses'.format(al))
else:
    print('Passou o seu prazo de alistamento há {} anos'. format(al))
