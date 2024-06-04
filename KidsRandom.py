from random import *
from time import sleep

Tom = 0
Oliver = 0
Sydney = 0
winner = 0
Rolls = list()

while  Tom < 2 and Oliver < 2 and Sydney < 2 :
    Roll = randint(1, 6)
    print("The roll is:", Roll)
    if Roll == 2 or Roll == 4:
        print("Tom gets a point!")
        Tom += 1
        continue

    elif Roll == 3 or Roll == 6:
        print("Oliver gets a point!")
        Oliver += 1
        continue

    elif Roll == 1 or Roll == 5:
        print("Sydney gets a point!")
        Sydney += 1
        continue
    else:
        print("Something went wrong!!!")
        continue
if Tom == 2:
    print("The winner is Tom!")
elif Oliver == 2:
    print("The winner is Oliver!")
elif Sydney:
    print("The winner is Sydney!")

sleep(10)