# tabuada usando o for
from time import sleep
tab= int(input(' Digite o número de 0 a 10, que eu mostrarei sua tabuada:'))

if tab==1:
    for c in range(1,11,1):
        print(c)
        sleep(0.5)

elif tab==2:
    for c in range(2,21,2):
        print(c)
        sleep(0.5)
elif tab==3:
    for c in range(3,31,3):
        print(c)
        sleep(0.5)
elif tab==4:
    for c in range(4,41,4):
        print(c)
        sleep(0.5)

elif tab==5:
    for c in range(5,51,5):
        print(c)
        sleep(0.5)

elif tab==6:
    for c in range(6,61,6):
        print(c)
        sleep(0.5)

elif tab==7:
    for c in range(7,71,7):
        print(c)
        sleep(0.5)

elif tab==8:
    for c in range(8,81,8):
        print(c)
        sleep(0.5)

elif tab==9:
    for c in range(9,91,9):
        print(c)
        sleep(0.5)

else:
    for c in range(10,101,10):
        print(c)
        sleep(0.5)