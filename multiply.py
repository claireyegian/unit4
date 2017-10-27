#Claire Yegian
#10/26/17
#multiply.py - teaches user how to multiply

from random import randint

def encourage():
    num3 = randint(1,4)
    if num3==1:
        return('Watch out world, here comes the next great multiplier!')
    if num3==2:
        return('Amazing job!')
    if num3==3:
        return('Keep up the great multiplying!')
    if num3==4:
        return('Thats 5 more correct! Congrats')

total = 0
while total<=12:
    num1 = randint(1,12)
    num2 = randint(1,12)
    answer = int(input(str(num1)+' x '+str(num2)+' = '))
    if num1*num2==answer:
        total += 1
        if total%5 == 0:
            print(encourage())
    
