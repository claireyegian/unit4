#Claire Yegian
#10/18/17
#printSquares.py - prints out grid of squares

print(+--+)
print(|  |)
print(+--+)

if i==1 and n==1:
    print(+--+)
    print(|  |)
    print(+--+)
elif i>1 and n==1:
    print('+--+'+'--+'*(i-1))
    print(|  |)
    print(+--+)

def printSquares(rows,columns):
    while n<=columns:
        if columns == 0:
            break
        if columns == 1:
            print('+--+')
            print('|  |')
            print('+--+')
            n+=1
        if columns > 1:
            print('+--+'+'--+'*columns-1)
            print('|  |'+'  |'*columns-1)
            print('+--+'+'--+'*columns-1)
            n+=1
    while i<=rows:
        if rows == 0:
            break
        if rows == 1:
            print('+--+')
            print('|  |')
            print('+--+')
            i+=1
        if rows > 1:
            print('+--+'+'--+'*columns-1)
            print('|  |'+'  |'*columns-1)
            print('+--+'+'--+'*columns-1)
            i+=1