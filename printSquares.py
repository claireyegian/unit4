#Claire Yegian
#10/18/17
#printSquares.py - prints out grid of squares

def printSquares(rows,columns):
    n = 0
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
    i = 0
    while i<=rows:
        if rows == 0:
            break
        if rows == 1:
            print('+--+')
            print('|  |')
            print('+--+')
            i+=1
        if rows > 1:
            print('+--+'+'--+'*rows-1)
            print('|  |'+'  |'*rows-1)
            print('+--+'+'--+'*rows-1)
            i+=1

printSquares(2,4)