#Claire Yegian
#10/30/17
#quiz4.py - does a bunch of random stuff

def csia():
    print('Computer science is awesome')
    print('Computer science is awesome')
    print('Computer science is awesome')
    print('Computer science is awesome')
    print('Computer science is awesome')

def average(num1,num2,num3):
    return((num1+num2+num3)/3)

def lastLetter(string):
    for ch in string:
        print(ch)

def same(arg1,arg2):
    if arg1==arg2:
        return('True')
    else:
        return('False')

csia()
print(average(1,2,3))
lastLetter('Smedinghoff') #I couldn't get this function to print only the last letter
print(same(2*3,7-1))
