#Claire Yegian
#10/26/17
#triangle.py - takes coordinates of the vertices of a triangle and produces area

xvalue1 = float(input('x1 = '))
xvalue2 = float(input('x2 = '))
xvalue3 = float(input('x3 = '))
yvalue1 = float(input('y1 = '))
yvalue2 = float(input('y2 = '))
yvalue3 = float(input('y3 = '))

def distance(x1,y1,x2,y2):
    return (((x2-x1)**2+(y2-y1)**2)**(1/2))

lengtha = distance(xvalue1,yvalue1,xvalue2,yvalue2)
lengthb = distance(xvalue1,yvalue1,xvalue3,yvalue3)
lengthc = distance(xvalue2,yvalue2,xvalue3,yvalue3)

svalue = ((lengtha + lengthb + lengthc)/2)

area = (svalue*(svalue - lengtha)*(svalue - lengthb)*(svalue - lengthc))**(1/2)
print(area)