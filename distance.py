#Claire Yegian
#10/26/17
#distance.py - takes two points and finds distance between

def distance(x1,y1,x2,y2):
    return (((x2-x1)**2+(y2-y1)**2)**(1/2))

print(distance(3,4,-5,2))