#Claire Yegian
#10/18/17
#printStars.py - prints input number of stars in pyramid

def printnStars(num1):
    i=1
    while i<=num1:
        for t in range(num1,0,-1):
            print(' '*t+'*'*i+'*'*i)
            i += 1

printnStars(12)