#Claire Yegian
#10/17/17
#functionDemo.py - learning functions

def hw():
    print('Hello, world!')

def bigger(num1,num2): #prints which number is bigger
    if num1>num2:
        print(num1)
    else:
        print(num2)

def slope(x1,y1,x2,y2): #calculates slope
    print((y2-y1)/(x2-x1))

#tests for the various functions
hw()
bigger(13,27)
bigger(-10,-15)
bigger('Smeds','Yegian')
slope(1,2,2,4)
