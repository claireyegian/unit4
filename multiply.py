#Claire Yegian
#10/26/17
#multiply.py - teaches user how to multiply

from random import randint

num1 = randint(1,12)
num2 = randint(1,12)

def encourage():
    num3 = randint(1,4)
    if num3==1:
        return('Watch out world, here comes the next great multiplier!')
    if num3==2:
        return('Amazing job!')
    if num3==3:
        return('Keep up the great multiplying!')
    if num3==4:
        return('Thats 5 correct! Congrats')

total = 0
while true:
    answer = int(input(num1,'x',num2,'='))
    if num1*num2==answer:
        total += 1
        if total == 5:
            print(encourage())
    if answer=='break':
        break
    
